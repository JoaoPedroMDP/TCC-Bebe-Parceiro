#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.access_code_utils import create_n_access_codes


@pytest.mark.django_db
def test_can_list_all_access_codes(client):
    codes = create_n_access_codes(prefix="TCLAC", n=10)

    url = reverse("gen_access_codes")
    response = client.get(url)
    assert len(response.data) == len(codes)
