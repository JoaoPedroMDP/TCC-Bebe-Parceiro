#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import StateFactory


@pytest.mark.django_db
def test_can_list_all_states(client):
    states = StateFactory.create_batch(size=10)

    url = reverse("gen_states")
    response = client.get(url)
    assert len(response.data) == len(states)
