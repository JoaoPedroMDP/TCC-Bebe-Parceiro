#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import CountryFactory


@pytest.mark.django_db
def test_can_filter_countries_by_enabled(client: Client):
    CountryFactory.create_batch(size=5, enabled=False)
    CountryFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_countries")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
