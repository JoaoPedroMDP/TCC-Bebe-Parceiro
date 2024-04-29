#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_MARITAL_STATUSES
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_create_marital_status(client: APIClient):
    data = {'name': "TCCSP"}
    url = reverse('gen_marital_statuses')

    # Sem autenticação
    response = client.post(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_MARITAL_STATUSES]))
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
