#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import StateFactory


@pytest.mark.django_db
def test_can_filter_states_by_enabled(client: Client):
    StateFactory.create_batch(size=5, enabled=False)
    StateFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_states")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
