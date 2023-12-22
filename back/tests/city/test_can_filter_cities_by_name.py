#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import CityFactory


@pytest.mark.django_db
def test_can_filter_cities_by_name(client):
    CityFactory.create_batch(size=5)
    city_to_filter = CityFactory.create(name="TESTE")
    url = reverse("gen_cities")
    data = {"name": city_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == city_to_filter.name

