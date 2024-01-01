#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import CityFactory


@pytest.mark.django_db
def test_can_filter_cities_by_state_id(client: Client):
    city_to_filter = CityFactory.create()

    CityFactory.create_batch(size=5)

    url = reverse("gen_cities")
    data = {"state_id": city_to_filter.state.id}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == city_to_filter.name

