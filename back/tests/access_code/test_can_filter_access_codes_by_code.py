#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import AccessCodeFactory


@pytest.mark.django_db
def test_can_filter_access_codes_by_prefix(client):
    AccessCodeFactory.create_batch(size=5)
    code_to_filter = AccessCodeFactory.create()

    url = reverse("gen_access_codes")
    data = {"code": code_to_filter.code}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["code"] == code_to_filter.code
