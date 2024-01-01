#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse


@pytest.mark.django_db
def test_can_create_marital_status(client: Client):
    data = {'name': "TCCSP"}
    url = reverse('gen_marital_statuses')
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
