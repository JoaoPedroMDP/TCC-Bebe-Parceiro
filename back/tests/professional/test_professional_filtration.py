#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_PROFESSIONALS
from factories import ProfessionalFactory
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_filter_professional_by_speciality_id(client: APIClient):
    professional_to_filter = ProfessionalFactory.create()

    ProfessionalFactory.create_batch(size=5)

    url = reverse("gen_professionals")
    data = {"speciality_id": professional_to_filter.speciality.id}

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_volunteer([MANAGE_PROFESSIONALS]).user)
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == professional_to_filter.name


@pytest.mark.django_db
def test_can_filter_professionals_by_enabled(client: APIClient):
    ProfessionalFactory.create_batch(size=5, enabled=False)
    ProfessionalFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_professionals")
    data = {"enabled": True}

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_volunteer([MANAGE_PROFESSIONALS]).user)
    response = client.get(url, data=data)
    logging.info(response)
    assert len(response.data) == 3


@pytest.mark.django_db
def test_can_filter_professional_by_name(client: APIClient):
    ProfessionalFactory.create_batch(size=5)
    professional_to_filter = ProfessionalFactory.create(name="TESTE")

    url = reverse("gen_professionals")
    data = {"name": professional_to_filter.name}

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_volunteer([MANAGE_PROFESSIONALS]).user)
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == professional_to_filter.name
