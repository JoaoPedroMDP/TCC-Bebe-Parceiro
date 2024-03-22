#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import AccessCodeFactory


@pytest.mark.django_db
def test_can_get_access_code(client: Client):
    ac = AccessCodeFactory.create()
    url = reverse("spe_access_codes", kwargs={"pk": ac.id})

    response = client.get(url)
    print(response.data)
    assert response.status_code == 200
    assert response.data["code"] == ac.code
