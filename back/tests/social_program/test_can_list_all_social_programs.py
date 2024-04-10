#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_SOCIAL_PROGRAMS
from factories import SocialProgramFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_list_all_social_programs(client: APIClient):
    social_programs = SocialProgramFactory.create_batch(size=10)

    url = reverse("gen_social_programs")
    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_SOCIAL_PROGRAMS]))
    response = client.get(url)
    assert len(response.data) == len(social_programs)
