#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_ACCESS_CODES
from factories import AccessCodeFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_get_access_code(client: APIClient):
    ac = AccessCodeFactory.create()
    url = reverse("spe_access_codes", kwargs={"pk": ac.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user(["manage_access_codes"]))
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["code"] == ac.code
