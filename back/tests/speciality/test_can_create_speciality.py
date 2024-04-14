#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_SPECIALITIES
from factories import SpecialityFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_create_speciality(client: APIClient):
    data = {'name': "TCCS"}
    url = reverse('gen_specialities')

    # Sem autenticação
    response = client.post(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_SPECIALITIES]))
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
