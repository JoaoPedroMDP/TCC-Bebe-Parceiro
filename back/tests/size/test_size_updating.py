from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import MANAGE_SIZES
from factories import SizeFactory
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_update_size(client: APIClient):
    size = SizeFactory.create()
    data = {'name': "TCCS"}
    
    url = reverse('spe_sizes', args=[size.id])
    vol = make_volunteer([MANAGE_SIZES])
    client.force_authenticate(vol.user)

    response = client.patch(url, data=data)
    assert response.status_code == 200
    assert response.data['name'] == data["name"]
