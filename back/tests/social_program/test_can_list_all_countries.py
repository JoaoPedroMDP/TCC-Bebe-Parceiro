#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.social_program_utils import create_n_social_programs


@pytest.mark.django_db
def test_can_list_all_social_programs(client):
    social_programs = create_n_social_programs(name="TCLASP", n=10)

    url = reverse("gen_social_programs")
    response = client.get(url)
    assert len(response.data) == len(social_programs)
