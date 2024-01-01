#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse


@pytest.mark.django_db
def test_can_create_access_code(client: Client):
    data = {'prefix': "TCCAC"}
    url = reverse('gen_access_codes')
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['code'].startswith("TCCAC") is True
    assert response.data['used'] is False
