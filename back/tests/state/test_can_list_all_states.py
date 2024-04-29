#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import StateFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_list_all_states(client: APIClient):
    states = StateFactory.create_batch(size=10)
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))

    url = reverse("gen_states")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(states)
