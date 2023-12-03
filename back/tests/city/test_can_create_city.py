#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.state_utils import create_state


@pytest.mark.django_db
def test_can_create_city(client):
    test_state = create_state(name="TS")

    data = {'name': "TCCC", "state_id": test_state.id}
    url = reverse('gen_cities')
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
