#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import SocialProgramFactory


@pytest.mark.django_db
def test_can_list_all_social_programs(client):
    social_programs = SocialProgramFactory.create_batch(size=10)

    url = reverse("gen_social_programs")
    response = client.get(url)
    assert len(response.data) == len(social_programs)
