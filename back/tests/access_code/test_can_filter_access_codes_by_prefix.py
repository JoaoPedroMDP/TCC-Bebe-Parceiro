#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.access_code_utils import create_n_access_codes


@pytest.mark.django_db
def test_can_filter_access_codes_by_prefix(client):
    code_to_filter = create_n_access_codes(prefix="TCFAC", n=5)[2]

    url = reverse("gen_access_codes")
    data = {"code": code_to_filter.code}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["code"] == code_to_filter.code

