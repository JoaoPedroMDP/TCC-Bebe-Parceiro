#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.state_utils import create_n_states, mark_states_as_disabled


@pytest.mark.django_db
def test_can_filter_states_by_enabled(client):
    enabled_states = create_n_states(name="TCFSBE1", n=5)
    mark_states_as_disabled(enabled_states)
    create_n_states(name="TCFSBE2", n=3)

    url = reverse("gen_states")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
