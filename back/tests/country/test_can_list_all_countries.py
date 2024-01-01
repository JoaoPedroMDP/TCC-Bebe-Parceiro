#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import CountryFactory


@pytest.mark.django_db
def test_can_list_all_countries(client: Client):
    countries = CountryFactory.create_batch(size=5)

    url = reverse("gen_countries")
    response = client.get(url)
    assert len(response.data) == len(countries)
