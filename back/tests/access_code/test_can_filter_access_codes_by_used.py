#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import AccessCodeFactory


@pytest.mark.django_db
def test_can_filter_access_codes_by_used(client: Client):
    AccessCodeFactory.create_batch(size=5, used=True)
    AccessCodeFactory.create_batch(size=3, used=False)

    url = reverse("gen_access_codes")
    data = {"used": True}
    response = client.get(url, data=data)
    assert len(response.data) == 5
