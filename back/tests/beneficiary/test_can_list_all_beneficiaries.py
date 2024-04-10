#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_BENEFICIARIES
from factories import BeneficiaryFactory, CityFactory, MaritalStatusFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_list_all_beneficiaries(client: APIClient):
    city = CityFactory.create()
    marital = MaritalStatusFactory.create()

    beneficiaries = BeneficiaryFactory.create_batch(size=10, city=city, marital_status=marital)

    url = reverse("gen_beneficiaries")
    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401
    
    # Com autenticação
    client.force_authenticate(make_user([MANAGE_BENEFICIARIES]))
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(beneficiaries)
