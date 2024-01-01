#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import StateFactory


@pytest.mark.django_db
def test_can_filter_states_by_country_id(client: Client):
    state_to_filter = StateFactory.create()

    StateFactory.create_batch(size=5)

    url = reverse("gen_states")
    data = {"country_id": state_to_filter.country.id}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == state_to_filter.name

