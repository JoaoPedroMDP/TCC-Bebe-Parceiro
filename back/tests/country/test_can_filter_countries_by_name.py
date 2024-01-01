#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import CountryFactory


@pytest.mark.django_db
def test_can_filter_countries_by_name(client: Client):
    CountryFactory.create_batch(size=5)
    country_to_filter = CountryFactory.create(name="TESTE")

    url = reverse("gen_countries")
    data = {"name": country_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == country_to_filter.name

