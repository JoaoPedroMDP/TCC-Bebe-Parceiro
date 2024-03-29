#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ACCESS_CODES
from core.models import User
from tests.conftest import make_user

lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_create_access_code(client: APIClient):
    url = reverse('gen_access_codes')

    # Sem autenticação
    response = client.post(url)
    assert response.status_code == 401

    # Com autenticação
    user: User = make_user([MANAGE_ACCESS_CODES])
    client.force_authenticate(user)
    response = client.post(url)
    prefix = user.first_name[:3].upper()
    assert response.status_code == 201
    assert response.data[0]['code'].startswith(prefix) is True
    assert response.data[0]['used'] is False


@pytest.mark.django_db
def test_can_create_multiple_access_codes(client: APIClient):
    amount = 5
    data = {'prefix': "TCCMAC", "amount": amount}
    url = reverse('gen_access_codes')

    # Sem autenticação
    response = client.post(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ACCESS_CODES]))
    response = client.post(url, data=data)
    assert response.status_code == 201
    assert len(response.data) == amount
    for code in response.data:
        assert code['code'].startswith("TCCMAC") is True
        assert code['used'] is False
