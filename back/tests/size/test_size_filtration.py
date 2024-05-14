from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import MANAGE_SIZES
from factories import SizeFactory
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_filter_size_by_name(client: APIClient):
    SizeFactory.create_batch(5)
    size = SizeFactory.create(name="TCFSBN")
    
    url = reverse('gen_sizes')
    vol = make_volunteer([MANAGE_SIZES])
    client.force_authenticate(vol.user)

    response = client.get(url, {'name': size.name})
    assert response.status_code == 200
    assert len(response.data) == 1
