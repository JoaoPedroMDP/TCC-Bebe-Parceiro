#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CityFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_cities_by_name(client: APIClient):
    CityFactory.create_batch(size=5)
    city_to_filter = CityFactory.create(name="TESTE")

    url = reverse("gen_cities")
    data = {"name": city_to_filter.name}

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == city_to_filter.name

