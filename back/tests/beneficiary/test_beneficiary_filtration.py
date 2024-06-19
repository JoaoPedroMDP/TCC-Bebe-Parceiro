#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_BENEFICIARIES
from factories import BeneficiaryFactory, CityFactory, MaritalStatusFactory, SocialProgramFactory
from tests.conftest import make_beneficiary, make_user, make_volunteer


@pytest.mark.django_db
def test_can_filter_beneficiaries(client: APIClient):
    CityFactory.create_batch(3)
    MaritalStatusFactory.create_batch(3)
    SocialProgramFactory.create_batch(3)

    for _ in range(2):
        make_beneficiary(child_count=2)

    beneficiary = make_beneficiary(child_count=1)

    url = reverse("gen_beneficiaries")
    data = {"child_count": beneficiary.child_count}
    # Sem autenticação
    response = client.get(url, data=data, content_type='application/json')
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_BENEFICIARIES])
    client.force_authenticate(vol.user)
    response = client.get(url, data=data, content_type='application/json')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['child_count'] == beneficiary.child_count
