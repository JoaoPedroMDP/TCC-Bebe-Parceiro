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
    response = client.get(url)
    assert len(response.data) == len(social_programs)
