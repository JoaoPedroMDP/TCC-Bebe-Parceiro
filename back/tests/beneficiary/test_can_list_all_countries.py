#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import CountryFactory


@pytest.mark.django_db
def test_can_list_all_countries(client):
    countries = CountryFactory.create_batch(size=10)

    url = reverse("gen_countries")
    response = client.get(url)
    assert len(response.data) == len(countries)
