#  coding: utf-8
from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import APPROVED, MANAGE_EVALUATIONS
from core.models import Register
from factories import AppointmentFactory, StatusFactory
from tests.conftest import make_beneficiary, make_volunteer


@pytest.mark.django_db
def test_can_end_evaluation(client: APIClient):
    ben = make_beneficiary(approved=False)
    vol = make_volunteer([MANAGE_EVALUATIONS])
    appo = AppointmentFactory.create(beneficiary=ben, volunteer=vol)
    status = StatusFactory.create(name=APPROVED)
    
    url = reverse('end_evaluation', args=[appo.id])
    client.force_authenticate(user=vol.user)

    data = {
        'status_id': status.id,
        'description': 'Lorem ipsum dolor sit amet consectetur adipiscing elit.'
    }

    response = client.patch(url, data=data)
    assert response.status_code == 200
    register = Register.objects.filter(appointment=appo).first()
    assert register.description == data['description']