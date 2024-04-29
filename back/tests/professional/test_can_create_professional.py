#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_PROFESSIONALS
from factories import SpecialityFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_create_professional(client: APIClient):
    test_speciality = SpecialityFactory.create(name="TS")

    data = {'name': "TCCP", "speciality_id": test_speciality.id}
    url = reverse('gen_specialities')

    # Sem autenticação
    response = client.post(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_PROFESSIONALS]))
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
