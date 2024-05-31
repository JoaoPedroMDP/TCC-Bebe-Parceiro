#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_SPECIALITIES
from factories import SpecialityFactory
from tests.conftest import make_user, make_volunteer


@pytest.mark.django_db
def test_can_get_country(client: APIClient):
    speciality = SpecialityFactory.create(name="TCGS")
    url = reverse("spe_specialities", kwargs={"pk": speciality.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_SPECIALITIES])
    client.force_authenticate(vol.user)
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["name"] == speciality.name
