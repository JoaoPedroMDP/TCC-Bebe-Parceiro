#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CityFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_cities_by_state_id(client: APIClient):
    city_to_filter = CityFactory.create()

    CityFactory.create_batch(size=5)

    url = reverse("gen_cities")
    data = {"state_id": city_to_filter.state.id}

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == city_to_filter.name

