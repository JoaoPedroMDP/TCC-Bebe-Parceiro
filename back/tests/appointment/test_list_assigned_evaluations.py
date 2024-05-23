#  coding: utf-8
import logging

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_EVALUATIONS
from factories import AppointmentFactory
from tests.conftest import make_beneficiary, make_user, make_volunteer


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
@pytest.mark.permissions
def test_permissions(client: APIClient):
    url = reverse('assigned_evaluations')
    
    # Anônimo não passa
    response = client.get(url)
    assert response.status_code == 401

    # Beneficiária não passa
    ben = make_beneficiary()
    client.force_authenticate(user=ben.user)
    response = client.get(url)
    assert response.status_code == 403

    # Voluntária sem permissão não passa
    vol = make_volunteer()
    client.force_authenticate(user=vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Voluntária com permissão pode ver as avaliações designadas a ela
    vol = make_volunteer([MANAGE_EVALUATIONS])
    client.force_authenticate(user=vol.user)
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_vol_can_list_assigned_evaluations(client: APIClient):
    vol = make_volunteer([MANAGE_EVALUATIONS])
    ben = make_beneficiary()
    appointment = AppointmentFactory.create(beneficiary=ben, volunteer=vol)

    url = reverse('assigned_evaluations')
    client.force_authenticate(user=vol.user)

    response = client.get(url)
    assert response.status_code == 200
    assert response.data[0]['id'] == appointment.id
