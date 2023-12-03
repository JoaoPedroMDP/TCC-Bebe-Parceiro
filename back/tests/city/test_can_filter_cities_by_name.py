#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.city_utils import create_n_cities


@pytest.mark.django_db
def test_can_filter_cities_by_name(client):
    city_to_filter = create_n_cities(name="TCFCN", n=5)[2]

    url = reverse("gen_cities")
    data = {"name": city_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == city_to_filter.name

