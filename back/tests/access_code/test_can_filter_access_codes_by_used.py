#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.access_code_utils import create_n_access_codes, mark_codes_as_used


@pytest.mark.django_db
def test_can_filter_access_codes_by_used(client):
    used_codes = create_n_access_codes(prefix="TCFAC", n=5)
    mark_codes_as_used(used_codes)
    create_n_access_codes(prefix="TCFAC", n=3)

    url = reverse("gen_access_codes")
    data = {"used": True}
    response = client.get(url, data=data)
    assert len(response.data) == 5
