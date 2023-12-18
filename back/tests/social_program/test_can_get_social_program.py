#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.social_program_utils import create_social_program


@pytest.mark.django_db
def test_can_get_social_program(client):
    social_program = create_social_program(name="TCGSP")
    url = reverse("spe_social_programs", kwargs={"pk": social_program.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == social_program.name
