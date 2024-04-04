#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CountryFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_get_country(client: APIClient):
    country = CountryFactory.create(name="TCGC")
    url = reverse("spe_countries", kwargs={"pk": country.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["name"] == country.name
