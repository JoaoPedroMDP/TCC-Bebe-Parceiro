#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.city_utils import create_n_cities


@pytest.mark.django_db
def test_can_list_all_cities(client):
    cities = create_n_cities(name="TCLAC", n=10)

    url = reverse("gen_cities")
    response = client.get(url)
    assert len(response.data) == len(cities)
