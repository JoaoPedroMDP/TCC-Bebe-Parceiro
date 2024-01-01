#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import StateFactory


@pytest.mark.django_db
def test_can_get_state(client: Client):
    state = StateFactory.create(name="TCGS")
    url = reverse("spe_states", kwargs={"pk": state.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == state.name
