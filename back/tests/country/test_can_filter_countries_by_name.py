#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.country_utils import create_n_countries


@pytest.mark.django_db
def test_can_filter_countries_by_name(client):
    country_to_filter = create_n_countries(name="TCFCN", n=5)[2]

    url = reverse("gen_countries")
    data = {"name": country_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == country_to_filter.name

