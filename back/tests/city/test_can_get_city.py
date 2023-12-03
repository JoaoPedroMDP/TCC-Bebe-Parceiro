#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.city_utils import create_city


@pytest.mark.django_db
def test_can_get_city(client):
    city = create_city(name="TCGC")
    url = reverse("spe_cities", kwargs={"pk": city.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == city.name
