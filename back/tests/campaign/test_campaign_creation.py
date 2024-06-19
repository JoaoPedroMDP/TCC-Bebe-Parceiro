#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_CAMPAIGNS
from tests.conftest import make_user, make_volunteer


@pytest.mark.django_db
def test_can_create_campaign(client: APIClient):
    data = {'name': 'TCCCampanha', 'start_date': '2021-01-01', 'end_date': '2021-12-31', 'description': 'Teste de campanha'}
    url = reverse('gen_campaigns')

    # Sem autenticação
    response = client.post(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['start_date'] == data["start_date"]
    assert response.data['end_date'] == data["end_date"]
    assert response.data['description'] == data["description"]
    assert response.data['external_link'] is None

