#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.country_utils import create_n_countries, mark_countries_as_disabled


@pytest.mark.django_db
def test_can_filter_countries_by_enabled(client):
    enabled_countries = create_n_countries(name="TCFCBE1", n=5)
    mark_countries_as_disabled(enabled_countries)
    create_n_countries(name="TCFCBE2", n=3)

    url = reverse("gen_countries")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
