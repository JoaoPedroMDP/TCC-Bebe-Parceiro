#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_SOCIAL_PROGRAMS
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_create_social_program(client: APIClient):
    data = {'name': "TCCSP"}
    url = reverse('gen_social_programs')
    response = client.post(url, data=data)

    # Sem autenticação
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_SOCIAL_PROGRAMS]))
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
