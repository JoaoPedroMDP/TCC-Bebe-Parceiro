from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_CAMPAIGNS
from tests.conftest import make_beneficiary, make_volunteer

@pytest.mark.django_db
@pytest.mark.permissions
def test_campaign_gen_get_permissions(client: APIClient):
    url = reverse('gen_campaigns')
    
    # Anônimos não passam
    response = client.get(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Beneficiárias passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 200

    # Voluntárias com permissão podem listar todas as Campanhas
    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.permissions
def test_campaign_gen_post_permissions(client: APIClient):
    url = reverse('gen_campaigns')

    # Anônimos não passam
    response = client.post(url)
    assert response.status_code == 401

    # Beneficiárias não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.post(url)
    assert response.status_code == 403

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.post(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem criar Campanhas
    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)
    response = client.post(url)
    assert response.status_code == 400

@pytest.mark.django_db
@pytest.mark.permissions
def test_campaign_spe_get_permissions(client: APIClient):
    url = reverse('spe_campaigns', kwargs={'pk': 1})

    # Anônimos não passam
    response = client.get(url)
    assert response.status_code == 401

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Beneficiárias passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 404

    # Voluntárias com permissão podem visualizar uma Campanha específica
    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
@pytest.mark.permissions
def test_campaign_spe_patch_permissions(client: APIClient):
    url = reverse('spe_campaigns', kwargs={'pk': 1})

    # Anônimos não passam
    response = client.patch(url)
    assert response.status_code == 401

    # Beneficiárias não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem editar uma Campanha
    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)
    response = client.patch(url)
    assert response.status_code == 404

@pytest.mark.django_db
@pytest.mark.permissions
def test_campaign_spe_delete_permissions(client: APIClient):
    url = reverse('spe_campaigns', kwargs={'pk': 1})

    # Anônimos não passam
    response = client.delete(url)
    assert response.status_code == 401

    # Beneficiárias não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.delete(url)
    assert response.status_code == 403

    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.delete(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem deletar uma Campanha
    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)
    response = client.delete(url)
    assert response.status_code == 404
