from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from tests.conftest import make_beneficiary, make_city, make_volunteer


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


@pytest.mark.django_db
def test_city_spe_patch_permissions(client: APIClient):
    city = make_city(name='Maringa')
    url = reverse('spe_cities', kwargs={'pk': city.id})

    # Anônimos não passam
    response = client.patch(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 403
    
    # Beneficiárias não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem editar cidades
    vol = make_volunteer([MANAGE_ADDRESSES])
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 400


@pytest.mark.django_db
def test_city_spe_delete_permissions(client: APIClient):
    city = make_city(name='Maringa')
    url = reverse('spe_cities', kwargs={'pk': city.id})

    # Anônimos não passam
    response = client.delete(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.delete(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.delete(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem deletar cidades
    vol = make_volunteer([MANAGE_ADDRESSES])
    client.force_authenticate(vol.user)
    response = client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_city_spe_get_permissions(client: APIClient):
    city = make_city(name='Maringa')
    url = reverse('spe_cities', kwargs={'pk': city.id})

    # Anônimos não passam
    response = client.get(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem visualizar uma cidade
    vol = make_volunteer([MANAGE_ADDRESSES])
    client.force_authenticate(vol.user)
    response = client.get(url)
    print(response.data)
    assert response.status_code == 200
