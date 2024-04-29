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

    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == state_to_filter.name


@pytest.mark.django_db
def test_can_filter_states_by_enabled(client: APIClient):
    StateFactory.create_batch(size=5, enabled=False)
    StateFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_states")
    data = {"enabled": True}

    response = client.get(url, data=data)
    assert len(response.data) == 3


@pytest.mark.django_db
def test_can_filter_states_by_name(client: APIClient):
    StateFactory.create_batch(size=5)
    state_to_filter = StateFactory.create(name="TESTE")

    url = reverse("gen_states")
    data = {"name": state_to_filter.name}

    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == state_to_filter.name
