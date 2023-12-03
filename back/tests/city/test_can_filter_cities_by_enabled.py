#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.city_utils import create_n_cities, mark_cities_as_disabled


@pytest.mark.django_db
def test_can_filter_cities_by_enabled(client):
    enabled_cities = create_n_cities(name="TCFCBE1", n=5)
    mark_cities_as_disabled(enabled_cities)
    create_n_cities(name="TCFCBE2", n=3)

    url = reverse("gen_cities")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
