#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_create_country(client: APIClient):
    data = {'name': "TCCC"}
    url = reverse('gen_countries')

    # Com autenticação
    client.force_authenticate(make_volunteer([MANAGE_ADDRESSES]).user)
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
