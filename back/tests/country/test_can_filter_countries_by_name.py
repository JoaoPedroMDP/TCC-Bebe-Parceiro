#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CountryFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_countries_by_name(client: APIClient):
    CountryFactory.create_batch(size=5)
    country_to_filter = CountryFactory.create(name="TESTE")

    url = reverse("gen_countries")
    data = {"name": country_to_filter.name}

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == country_to_filter.name

