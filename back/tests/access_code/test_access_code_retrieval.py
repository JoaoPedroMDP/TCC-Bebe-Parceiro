#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_ACCESS_CODES
from factories import AccessCodeFactory
from tests.conftest import make_user, make_volunteer


@pytest.mark.django_db
def test_can_get_access_code(client: APIClient):
    ac = AccessCodeFactory.create()
    
    url = reverse("spe_access_codes", kwargs={"pk": ac.id})
    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["code"] == ac.code
