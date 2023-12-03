#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.state_utils import create_n_states


@pytest.mark.django_db
def test_can_list_all_states(client):
    states = create_n_states(name="TCLAS", n=10)

    url = reverse("gen_states")
    response = client.get(url)
    assert len(response.data) == len(states)
