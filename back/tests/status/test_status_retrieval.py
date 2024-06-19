from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from factories import StatusFactory
from tests.conftest import make_beneficiary, make_volunteer


@pytest.mark.django_db
def test_vol_can_get_status(client: APIClient):
    status = StatusFactory.create()
    
    vol = make_volunteer()
    client.force_authenticate(user=vol.user)
    url = reverse('spe_status', kwargs={"pk": status.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == status.name


@pytest.mark.django_db
def test_ben_can_get_status(client: APIClient):
    status = StatusFactory.create()
    
    ben = make_beneficiary()
    client.force_authenticate(user=ben.user)
    url = reverse('spe_status', kwargs={"pk": status.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == status.name
