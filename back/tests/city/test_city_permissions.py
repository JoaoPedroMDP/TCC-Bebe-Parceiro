from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from tests.conftest import make_beneficiary, make_volunteer


@pytest.mark.django_db
def test_city_gen_get_permissions(client: APIClient):
    url = reverse('gen_cities')

    # Anônimos passam
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_city_gen_post_permissions(client: APIClient):
    url = reverse('gen_cities')

    # Anônimos não passam
    response = client.post(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.post(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.post(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem criar cidades
    vol = make_volunteer([MANAGE_ADDRESSES])
    client.force_authenticate(vol.user)
    response = client.post(url)
    assert response.status_code == 400
