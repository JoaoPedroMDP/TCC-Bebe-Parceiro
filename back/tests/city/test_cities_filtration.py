#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CityFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_cities_by_enabled(client: APIClient):
    CityFactory.create_batch(size=5, enabled=False)
    CityFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_cities")
    data = {"enabled": True}

    response = client.get(url, data=data)
    assert len(response.data) == 3


@pytest.mark.django_db
def test_can_filter_cities_by_name(client: APIClient):
    CityFactory.create_batch(size=5)
    city_to_filter = CityFactory.create(name="TESTE")

    url = reverse("gen_cities")
    data = {"name": city_to_filter.name}

    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == city_to_filter.name


@pytest.mark.django_db
def test_can_filter_cities_by_state_id(client: APIClient):
    city_to_filter = CityFactory.create()

    CityFactory.create_batch(size=5)

    url = reverse("gen_cities")
    data = {"state_id": city_to_filter.state.id}

    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == city_to_filter.name
