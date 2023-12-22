#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import CityFactory


@pytest.mark.django_db
def test_can_get_city(client):
    city = CityFactory.create()
    url = reverse("spe_cities", kwargs={"pk": city.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == city.name
