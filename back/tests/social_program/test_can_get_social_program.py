#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_SOCIAL_PROGRAMS
from factories import SocialProgramFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_get_social_program(client: APIClient):
    social_program = SocialProgramFactory.create()
    url = reverse("spe_social_programs", kwargs={"pk": social_program.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_SOCIAL_PROGRAMS]))
    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == social_program.name
