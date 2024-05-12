import json
import logging
from django.urls import reverse
from rest_framework.test import APIClient


import pytest

from config import MANAGE_SWAPS, PENDING, ROLE_BENEFICIARY, ROLE_VOLUNTEER
from factories import BeneficiaryFactory, ChildFactory, SizeFactory, StatusFactory
from tests.conftest import make_user


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_create_swap(client: APIClient):
    StatusFactory.create(name=PENDING)
    b_user = make_user([ROLE_BENEFICIARY])
    ben = BeneficiaryFactory.create(user=b_user)
    children = ChildFactory.create_batch(2, beneficiary=ben)

    data = {
        "cloth_size_id": SizeFactory.create(name="RN").id,
        "shoe_size_id": SizeFactory.create(name="16").id,
        "description": "Troca de roupas e sapatos",
        "child_id": children[0].id
    }

    url = reverse('gen_swaps')
    # Sem autenticação
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(user=b_user)
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    lgr.debug(response.data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_cannot_create_swap_for_another_beneficiary_child(client: APIClient):
    StatusFactory.create(name=PENDING)
    b1_user = make_user([ROLE_BENEFICIARY])
    ben1 = BeneficiaryFactory.create(user=b1_user)
    
    b2_user = make_user([ROLE_BENEFICIARY])
    ben = BeneficiaryFactory.create(user=b2_user)
    children = ChildFactory.create_batch(2, beneficiary=ben)

    data = {
        "cloth_size_id": SizeFactory.create(name="RN").id,
        "shoe_size_id": SizeFactory.create(name="16").id,
        "description": "Troca de roupas e sapatos",
        "child_id": children[1].id
    }

    url = reverse('gen_swaps')
    client.force_authenticate(user=b1_user)
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['message'] == "A criança não pertence à beneficiária"


@pytest.mark.django_db
def test_cannot_create_more_than_one_swap_per_ben(client: APIClient):
    StatusFactory.create(name=PENDING)
    b_user = make_user([ROLE_BENEFICIARY])
    ben = BeneficiaryFactory.create(user=b_user)
    children = ChildFactory.create_batch(2, beneficiary=ben)

    data = {
        "cloth_size_id": SizeFactory.create(name="RN").id,
        "shoe_size_id": SizeFactory.create(name="16").id,
        "description": "Troca de roupas e sapatos",
        "child_id": children[0].id
    }

    url = reverse('gen_swaps')
    client.force_authenticate(user=b_user)
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['message'] == "Beneficiária já possui uma troca pendente"


@pytest.mark.django_db
def test_volunteer_must_specify_beneficiary(client: APIClient):
    StatusFactory.create(name=PENDING)
    b_user = make_user([ROLE_BENEFICIARY])
    ben = BeneficiaryFactory.create(user=b_user)
    children = ChildFactory.create_batch(2, beneficiary=ben)

    data = {
        "cloth_size_id": SizeFactory.create(name="RN").id,
        "shoe_size_id": SizeFactory.create(name="16").id,
        "description": "Troca de roupas e sapatos",
        "child_id": children[0].id
    }

    url = reverse('gen_swaps')

    client.force_authenticate(user=make_user([ROLE_VOLUNTEER, MANAGE_SWAPS]))
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['message'] == "Beneficiária não especificada"

    data['beneficiary_id'] = ben.id
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
