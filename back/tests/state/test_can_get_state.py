#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import StateFactory
from tests.conftest import make_user, make_volunteer


@pytest.mark.django_db
def test_can_get_state(client: APIClient):
    state = StateFactory.create(name="TCGS")
    url = reverse("spe_states", kwargs={"pk": state.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_ADDRESSES])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == state.name
