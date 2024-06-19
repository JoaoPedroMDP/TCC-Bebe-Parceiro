from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import MANAGE_SIZES
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_create_size(client: APIClient):
    data = {'name': "TCCS", "type": "CLOTH"}

    url = reverse('gen_sizes')
    vol = make_volunteer([MANAGE_SIZES])
    client.force_authenticate(vol.user)

    response = client.post(url, data=data)
    assert response.status_code == 201
    assert response.data['name'] == data["name"]