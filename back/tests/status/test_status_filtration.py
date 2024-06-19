
from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from core.models import Status
from factories import StatusFactory
from tests.conftest import make_beneficiary, make_volunteer


def filter_status(client: APIClient, status: Status):
    url = reverse('gen_status')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 6

    params = {'enabled': 'true'}
    response = client.get(url, params)
    assert response.status_code == 200
    assert len(response.data) == 3

    params = {'name': status.name}
    response = client.get(url, params)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == status.name


@pytest.mark.django_db
def test_vol_can_filter_status(client: APIClient):
    enabled_status = StatusFactory.create_batch(3, enabled=True)
    disabled_status = StatusFactory.create_batch(3, enabled=False)
    
    vol = make_volunteer()
    client.force_authenticate(user=vol.user)
    filter_status(client, enabled_status[0])


@pytest.mark.django_db
def test_ben_can_filter_status(client: APIClient):
    enabled_status = StatusFactory.create_batch(3, enabled=True)
    disabled_status = StatusFactory.create_batch(3, enabled=False)

    ben = make_beneficiary()
    client.force_authenticate(user=ben.user)
    filter_status(client, enabled_status[0])
