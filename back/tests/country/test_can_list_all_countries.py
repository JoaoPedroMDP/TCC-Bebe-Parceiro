#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.country_utils import create_n_countries


@pytest.mark.django_db
def test_can_list_all_countries(client):
    countries = create_n_countries(name="TCLAC", n=10)

    url = reverse("gen_countries")
    response = client.get(url)
    assert len(response.data) == len(countries)
