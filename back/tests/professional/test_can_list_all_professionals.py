#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_PROFESSIONALS
from factories import ProfessionalFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_list_all_professionals(client: APIClient):
    professionals = ProfessionalFactory.create_batch(size=10)
    client.force_authenticate(make_user([MANAGE_PROFESSIONALS]))

    url = reverse("gen_professionals")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(professionals)
