#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import CityFactory


@pytest.mark.django_db
def test_can_list_all_cities(client):
    cities = CityFactory.create_batch(size=5)

    url = reverse("gen_cities")
    response = client.get(url)
    assert len(response.data) == len(cities)
