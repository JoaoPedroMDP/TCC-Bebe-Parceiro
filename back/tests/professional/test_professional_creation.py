#  coding: utf-8
import logging
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_PROFESSIONALS
from factories import SpecialityFactory
from tests.conftest import make_volunteer


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_create_professional(client: APIClient):
    test_speciality = SpecialityFactory.create(name="TS")

    data = {'name': "TCCP", "speciality_id": test_speciality.id, "accepted_volunteer_terms": True, 'phone': '123456789'}
    url = reverse('gen_professionals')

    # Com autenticação
    vol = make_volunteer([MANAGE_PROFESSIONALS])
    client.force_authenticate(vol.user)
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True


@pytest.mark.django_db
def test_cant_create_professional_without_accepting_terms(client: APIClient):
    test_speciality = SpecialityFactory.create(name="TS")

    data = {'name': "TCCPWAT", "speciality_id": test_speciality.id, "accepted_volunteer_terms": False, 'phone': '123456789'}
    url = reverse('gen_professionals')

    # Com autenticação
    vol = make_volunteer([MANAGE_PROFESSIONALS])
    client.force_authenticate(vol.user)
    response = client.post(url, data=data)

    assert response.status_code == 400
    lgr.debug(response.data)
    assert response.data['message'] == 'Termos de voluntariado não aceitos'
