#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_BENEFICIARIES
from factories import BeneficiaryFactory, CityFactory, MaritalStatusFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_get_beneficiary(client: APIClient):
    city = CityFactory.create()
    marital = MaritalStatusFactory.create()

    beneficiary = BeneficiaryFactory.create(city=city, marital_status=marital)
    url = reverse("spe_beneficiaries", kwargs={"pk": beneficiary.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_BENEFICIARIES]))
    response = client.get(url)
    assert response.status_code == 200
    assert response.data["user"]["name"] == beneficiary.user.name
