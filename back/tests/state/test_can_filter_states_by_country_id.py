#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.state_utils import create_n_states, create_state


@pytest.mark.django_db
def test_can_filter_states_by_country_id(client):
    state_to_filter = create_state(name="TCFSCI")

    create_n_states(name="TCFSCIN", n=5)

    url = reverse("gen_states")
    data = {"country_id": state_to_filter.country.id}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == state_to_filter.name
