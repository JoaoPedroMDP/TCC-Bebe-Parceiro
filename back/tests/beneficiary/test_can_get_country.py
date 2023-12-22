#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import CountryFactory


@pytest.mark.django_db
def test_can_get_country(client):
    country = CountryFactory.create(name="TCGC")
    url = reverse("spe_countries", kwargs={"pk": country.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == country.name
