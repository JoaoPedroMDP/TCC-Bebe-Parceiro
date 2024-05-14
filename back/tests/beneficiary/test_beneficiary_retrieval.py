#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_BENEFICIARIES
from factories import CityFactory, MaritalStatusFactory
from tests.conftest import make_beneficiary, make_volunteer


@pytest.mark.django_db
def test_can_get_beneficiary(client: APIClient):
    city = CityFactory.create()
    marital = MaritalStatusFactory.create()

    beneficiary = make_beneficiary()
    url = reverse("spe_beneficiaries", kwargs={"pk": beneficiary.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(beneficiary.user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['user']["name"] == beneficiary.user.name


@pytest.mark.django_db
def test_can_list_all_beneficiaries(client: APIClient):
    city = CityFactory.create()
    marital = MaritalStatusFactory.create()

    beneficiaries = []
    for _ in range(5):
        beneficiaries.append(make_beneficiary(city=city, marital_status=marital))

    url = reverse("gen_beneficiaries")
    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401
    
    vol = make_volunteer([MANAGE_BENEFICIARIES])

    # Com autenticação
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(beneficiaries)
