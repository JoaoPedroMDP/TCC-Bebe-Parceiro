#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_PROFESSIONALS
from factories import ProfessionalFactory
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_get_professional(client: APIClient):
    professional = ProfessionalFactory.create(name="TCGP")
    url = reverse("spe_professionals", kwargs={"pk": professional.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_volunteer([MANAGE_PROFESSIONALS]).user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == professional.name
