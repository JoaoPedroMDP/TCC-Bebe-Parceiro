#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CountryFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_countries_by_enabled(client: APIClient):
    CountryFactory.create_batch(size=5, enabled=False)
    CountryFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_countries")
    data = {"enabled": True}

    response = client.get(url, data=data)
    print(response.data)
    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_can_filter_countries_by_name(client: APIClient):
    CountryFactory.create_batch(size=5)
    country_to_filter = CountryFactory.create(name="TESTE")

    url = reverse("gen_countries")
    data = {"name": country_to_filter.name}

    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == country_to_filter.name


@pytest.mark.django_db
def test_can_list_all_countries(client: APIClient):
    countries = CountryFactory.create_batch(size=5)
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))

    url = reverse("gen_countries")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(countries)
