#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import StateFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_states_by_country_id(client: APIClient):
    state_to_filter = StateFactory.create()

    StateFactory.create_batch(size=5)

    url = reverse("gen_states")
    data = {"country_id": state_to_filter.country.id}

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == state_to_filter.name

