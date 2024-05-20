#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ACCESS_CODES
from tests.conftest import make_volunteer

lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_create_access_code(client: APIClient):
    data = {'amount': 1}

    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)

    url = reverse('gen_access_codes')
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data[0]['used'] is False


@pytest.mark.django_db
def test_can_create_multiple_access_codes(client: APIClient):
    amount = 5
    data = {"amount": amount}

    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)

    url = reverse('gen_access_codes')
    response = client.post(url, data=data)
    
    assert response.status_code == 201
    assert len(response.data) == amount
    for code in response.data:
        assert code['used'] is False
