#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CountryFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_countries_by_enabled(client: APIClient):
    CountryFactory.create_batch(size=5, enabled=False)
    CountryFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_countries")
    data = {"enabled": True}

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))
    response = client.get(url, data=data)
    assert len(response.data) == 3
