#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.city_utils import create_n_cities, create_city


@pytest.mark.django_db
def test_can_filter_cities_by_state_id(client):
    city_to_filter = create_city(name="TCFCSI")

    create_n_cities(name="TCFCSI", n=5)

    url = reverse("gen_cities")
    data = {"state_id": city_to_filter.state.id}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == city_to_filter.name

