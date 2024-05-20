
from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import MANAGE_ACCESS_CODES
from factories import AccessCodeFactory
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_delete_access_code(client: APIClient):
    ac = AccessCodeFactory.create()
    
    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)
    
    url = reverse("spe_access_codes", kwargs={"pk": ac.id})
    response = client.delete(url)

    assert response.status_code == 204
