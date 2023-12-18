#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.social_program_utils import create_n_social_programs, mark_social_programs_as_disabled


@pytest.mark.django_db
def test_can_filter_social_programs_by_enabled(client):
    enabled_social_programs = create_n_social_programs(name="TCFSPBE1", n=5)
    mark_social_programs_as_disabled(enabled_social_programs)
    create_n_social_programs(name="TCFSPBE2", n=3)

    url = reverse("gen_social_programs")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
