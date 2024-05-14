#  coding: utf-8
import logging
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_VOLUNTEERS
from core.models import Volunteer
from factories import VolunteerFactory
from tests.conftest import make_volunteer


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_list_all_volunteers(client: APIClient):
    volunteers = []
    for _ in range(5):
        volunteers.append(make_volunteer())

    url = reverse("gen_volunteers")

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_VOLUNTEERS])
    volunteers.append(vol)
    
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert len(response.data) == len(volunteers)


@pytest.mark.django_db
def test_can_get_volunteer(client: APIClient):
    volunteer: Volunteer = make_volunteer()
    url = reverse("spe_volunteers", kwargs={"pk": volunteer.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_VOLUNTEERS])
    client.force_authenticate(vol.user)
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['user']["name"] == volunteer.user.name
