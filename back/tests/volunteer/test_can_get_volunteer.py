#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_VOLUNTEERS
from core.models import Volunteer
from factories import VolunteerFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_get_volunteer(client: APIClient):
    volunteer: Volunteer = VolunteerFactory.create()
    url = reverse("spe_volunteers", kwargs={"pk": volunteer.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_VOLUNTEERS]))
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['user']["name"] == volunteer.user.name
