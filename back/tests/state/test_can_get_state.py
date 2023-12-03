#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.state_utils import create_state


@pytest.mark.django_db
def test_can_get_state(client):
    state = create_state(name="TCGC")
    url = reverse("spe_states", kwargs={"pk": state.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == state.name
