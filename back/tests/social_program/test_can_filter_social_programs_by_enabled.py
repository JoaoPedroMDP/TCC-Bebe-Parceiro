#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import SocialProgramFactory


@pytest.mark.django_db
def test_can_filter_social_programs_by_enabled(client: Client):
    SocialProgramFactory.create_batch(size=5, enabled=False)
    SocialProgramFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_social_programs")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
