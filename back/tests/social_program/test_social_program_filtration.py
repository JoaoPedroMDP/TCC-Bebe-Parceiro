#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_SOCIAL_PROGRAMS
from factories import SocialProgramFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_social_programs_by_enabled(client: APIClient):
    SocialProgramFactory.create_batch(size=5, enabled=False)
    SocialProgramFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_social_programs")
    data = {"enabled": True}

    response = client.get(url, data=data)
    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_can_filter_social_programs_by_name(client: APIClient):
    SocialProgramFactory.create_batch(size=5)
    social_program_to_filter = SocialProgramFactory.create(name="TESTE")

    url = reverse("gen_social_programs")
    data = {"name": social_program_to_filter.name}

    response = client.get(url, data=data)

    assert len(response.data) == 1
    assert response.data[0]["name"] == social_program_to_filter.name
