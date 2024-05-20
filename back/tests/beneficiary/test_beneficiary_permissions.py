#  coding: utf-8
from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import MANAGE_BENEFICIARIES
from tests.conftest import make_beneficiary, make_volunteer


@pytest.mark.django_db
@pytest.mark.permissions
def test_beneficiary_gen_get(client: APIClient):
    # Anônimos não passam
    url = reverse('gen_beneficiaries')
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

    # Voluntárias com permissão podem listar todas as beneficiárias
    vol = make_volunteer([MANAGE_BENEFICIARIES])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.permissions
def test_beneficiary_gen_post(client: APIClient):
    # Anônimos passam
    url = reverse('gen_beneficiaries')
    response = client.post(url)
    assert response.status_code == 400


@pytest.mark.django_db
@pytest.mark.permissions
def test_beneficiary_gen_post_by_volunteer(client: APIClient):
    # Anônimos não passam
    url = reverse('create_beneficiaries')
    response = client.post(url)
    assert response.status_code == 401

    # Beneficiadas não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.post(url)
    assert response.status_code == 403

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.post(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem criar beneficiárias
    vol = make_volunteer([MANAGE_BENEFICIARIES])
    client.force_authenticate(vol.user)
    response = client.post(url)
    assert response.status_code == 400


@pytest.mark.django_db
@pytest.mark.permissions
def test_beneficiary_spe_get(client: APIClient):
    ben = make_beneficiary()
    url = reverse('spe_beneficiaries', kwargs={'pk': ben.id})

    # Anônimos não passam
    response = client.get(url)
    assert response.status_code == 401

    # Beneficiárias não podem ver outras beneficiárias
    ben_2 = make_beneficiary()
    client.force_authenticate(ben_2.user)
    response = client.get(url)
    assert response.status_code == 403

    # Voluntárias sem permissão não podem ver
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem ver
    vol = make_volunteer([MANAGE_BENEFICIARIES])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200

    # Beneficiárias podem ver a si mesmas
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.permissions
def test_beneficiary_spe_patch(client: APIClient):
    ben = make_beneficiary()
    url = reverse('spe_beneficiaries', kwargs={'pk': ben.id})
    
    # Anônimos não passam
    response = client.patch(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não podem editar
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 403
    
    # Beneficiárias não podem editar outras beneficiárias
    ben_2 = make_beneficiary()
    client.force_authenticate(ben_2.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem editar
    vol = make_volunteer([MANAGE_BENEFICIARIES])
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 200

    # Beneficiárias podem editar a si mesmas
    client.force_authenticate(ben.user)
    response = client.patch(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.permissions
def test_beneficiary_spe_delete(client: APIClient):
    ben = make_beneficiary()
    url = reverse('spe_beneficiaries', kwargs={'pk': ben.id})

    # Anônimos não passam
    response = client.delete(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não podem deletar
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.delete(url)
    assert response.status_code == 403

    # Beneficiárias não podem anonimizar outras beneficiárias
    ben_2 = make_beneficiary()
    client.force_authenticate(ben_2.user)
    response = client.delete(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem deletar
    vol = make_volunteer([MANAGE_BENEFICIARIES])
    client.force_authenticate(vol.user)
    response = client.delete(url)
    assert response.status_code == 204
    assert response.data['message'] == "Beneficiária deletada."

    # Beneficiárias podem anonimizar a si mesmas. Preciso criar de novo pois a outra foi removida
    ben = make_beneficiary()
    url = reverse('spe_beneficiaries', kwargs={'pk': ben.id})
    client.force_authenticate(ben.user)
    response = client.delete(url)
    assert response.status_code == 204
    assert response.data['message'] == "Beneficiária anonimizada."


def test_beneficiary_approval(client: APIClient):
    ben = make_beneficiary(approved=False)
    url = reverse('approve_beneficiaries', kwargs={'pk': ben.id})

    # Anônimos não passam
    response = client.patch(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    client.force_authenticate(ben.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem aprovar
    vol = make_volunteer([MANAGE_BENEFICIARIES])
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 400


def test_beneficiary_list_pending(client: APIClient):
    url = reverse('pending_beneficiaries')

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

    # Voluntárias com permissão podem ver
    vol = make_volunteer([MANAGE_BENEFICIARIES])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200


def test_beneficiary_swap_check(client: APIClient):
    url = reverse('can_request_swap_beneficiaries')

    # Anônimos não passam
    response = client.get(url)
    assert response.status_code == 401

    # Voluntárias não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Beneficiárias passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 200
