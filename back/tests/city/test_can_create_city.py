#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import StateFactory


@pytest.mark.django_db
def test_can_create_city(client: Client):
    test_state = StateFactory.create()

    data = {'name': "TCCC", "state_id": test_state.id}
    url = reverse('gen_cities')
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
