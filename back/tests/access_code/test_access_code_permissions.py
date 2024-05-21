
from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import MANAGE_ACCESS_CODES
from tests.conftest import make_volunteer


# Listagem e criação: Apenas as voluntárias com MANAGE_ACCESS_CODES
# Atualização, resgate e deleção: Apenas as voluntárias com MANAGE_ACCESS_CODES

@pytest.mark.django_db
@pytest.mark.permissions
def test_access_code_gen_get_permissions(client: APIClient):
    url = reverse('gen_access_codes')
    
    # Anônimos não passam
    response = client.get(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_volunteer()
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem listar todos os Códigos de Acesso
    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.permissions
def test_access_code_gen_post_permissions(client: APIClient):
    url = reverse('gen_access_codes')

    # Anônimos não passam
    response = client.post(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.post(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_volunteer()
    client.force_authenticate(ben.user)
    response = client.post(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem criar Códigos de Acesso
    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)
    response = client.post(url)
    assert response.status_code == 201


@pytest.mark.django_db
@pytest.mark.permissions
def test_access_code_spe_get_permissions(client: APIClient):
    url = reverse('spe_access_codes', kwargs={'pk': 1})

    # Anônimos não passam
    response = client.get(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_volunteer()
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem ver um Código de Acesso específico
    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
@pytest.mark.permissions
def test_access_code_spe_patch_permissions(client: APIClient):
    url = reverse('spe_access_codes', kwargs={'pk': 1})

    # Anônimos não passam
    response = client.patch(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_volunteer()
    client.force_authenticate(ben.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem atualizar um Código de Acesso específico
    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 404


@pytest.mark.django_db
@pytest.mark.permissions
def test_access_code_spe_delete_permissions(client: APIClient):
    url = reverse('spe_access_codes', kwargs={'pk': 1})

    # Anônimos não passam
    response = client.delete(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.delete(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_volunteer()
    client.force_authenticate(ben.user)
    response = client.delete(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem deletar um Código de Acesso específico
    vol = make_volunteer([MANAGE_ACCESS_CODES])
    client.force_authenticate(vol.user)
    response = client.delete(url)
    assert response.status_code == 404


@pytest.mark.django_db
@pytest.mark.permissions
def test_access_code_checking_permissions(client: APIClient):
    url = reverse('check_access_code')

    # Anônimos passam
    response = client.get(url)
    assert response.status_code == 400
