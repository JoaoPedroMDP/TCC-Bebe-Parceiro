#  coding: utf-8
from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import APPROVED, FINISHED, MANAGE_EVALUATIONS
from core.models import Register
from factories import AppointmentFactory, StatusFactory
from tests.conftest import make_beneficiary, make_volunteer

@pytest.mark.django_db
@pytest.mark.permissions
def test_can_end_evaluation_permissions(client: APIClient):
    url = reverse('end_evaluation', args=[1])

    # Anônimo não passa
    response = client.patch(url)
    assert response.status_code == 401

    # Beneficiária não passa
    ben = make_beneficiary()
    client.force_authenticate(user=ben.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Voluntária sem permissão não passa
    vol = make_volunteer()
    client.force_authenticate(user=vol.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Voluntária com permissão pode finalizar avaliação
    vol = make_volunteer([MANAGE_EVALUATIONS])
    client.force_authenticate(user=vol.user)
    response = client.patch(url)
    assert response.status_code == 400


@pytest.mark.django_db
def test_can_end_evaluation(client: APIClient):
    ben = make_beneficiary(approved=False)
    vol = make_volunteer([MANAGE_EVALUATIONS])
    appo = AppointmentFactory.create(beneficiary=ben, volunteer=vol)
    approved_status = StatusFactory.create(name=APPROVED)
    finished_status = StatusFactory.create(name=FINISHED)

    url = reverse('end_evaluation', args=[appo.id])
    client.force_authenticate(user=vol.user)

    data = {
        'status_id': approved_status.id,
        'description': 'Lorem ipsum dolor sit amet consectetur adipiscing elit.'
    }

    response = client.patch(url, data=data)
    assert response.status_code == 200
    register = Register.objects.filter(appointment=appo).first()
    assert register.description == data['description']
    appo.refresh_from_db()
    assert appo.status_id == finished_status.id