#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import CityFactory


@pytest.mark.django_db
def test_can_filter_cities_by_enabled(client):
    CityFactory.create_batch(size=5, enabled=False)
    CityFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_cities")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
