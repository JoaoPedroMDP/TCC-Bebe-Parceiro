#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.social_program_utils import create_n_social_programs


@pytest.mark.django_db
def test_can_filter_social_programs_by_name(client):
    social_program_to_filter = create_n_social_programs(name="TCFSPBN", n=5)[2]

    url = reverse("gen_social_programs")
    data = {"name": social_program_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == social_program_to_filter.name

