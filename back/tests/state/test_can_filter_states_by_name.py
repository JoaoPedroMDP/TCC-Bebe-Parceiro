#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.state_utils import create_n_states


@pytest.mark.django_db
def test_can_filter_states_by_name(client):
    state_to_filter = create_n_states(name="TCFSN", n=5)[2]

    url = reverse("gen_states")
    data = {"name": state_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == state_to_filter.name

