#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import SocialProgramFactory


@pytest.mark.django_db
def test_can_get_social_program(client: Client):
    social_program = SocialProgramFactory.create()
    url = reverse("spe_social_programs", kwargs={"pk": social_program.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == social_program.name
