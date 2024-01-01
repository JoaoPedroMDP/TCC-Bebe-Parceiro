#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import AccessCodeFactory


@pytest.mark.django_db
def test_can_list_all_access_codes(client: Client):
    codes = AccessCodeFactory.create_batch(size=5)

    url = reverse("gen_access_codes")
    response = client.get(url)
    assert len(response.data) == len(codes)
