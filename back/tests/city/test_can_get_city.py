#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CityFactory
from tests.conftest import make_user, make_volunteer


@pytest.mark.django_db
def test_can_get_city(client: APIClient):
    city = CityFactory.create(name="TCGC")
    url = reverse("spe_cities", kwargs={"pk": city.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_ADDRESSES])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == city.name
