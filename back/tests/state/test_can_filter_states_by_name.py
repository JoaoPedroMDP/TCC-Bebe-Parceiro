#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import StateFactory


@pytest.mark.django_db
def test_can_filter_states_by_name(client):
    StateFactory.create_batch(size=5)
    state_to_filter = StateFactory.create(name="TESTE")

    url = reverse("gen_states")
    data = {"name": state_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == state_to_filter.name

