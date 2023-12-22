#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import SocialProgramFactory


@pytest.mark.django_db
def test_can_filter_social_programs_by_name(client):
    SocialProgramFactory.create_batch(size=5)
    social_program_to_filter = SocialProgramFactory.create(name="TESTE")

    url = reverse("gen_social_programs")
    data = {"name": social_program_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == social_program_to_filter.name

