import json
import logging
from django.urls import reverse
from rest_framework.test import APIClient


import pytest

from config import APPROVED, MANAGE_SWAPS, PENDING
from factories import ChildFactory, SizeFactory, StatusFactory
from tests.conftest import make_beneficiary, make_less_than_one_year_child, make_volunteer


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_ben_can_create_swap(client: APIClient):
    StatusFactory.create(name=PENDING)
    ben = make_beneficiary()
    child = make_less_than_one_year_child(beneficiary=ben)

    data = {
        "cloth_size_id": SizeFactory.create(name="RN").id,
        "shoe_size_id": SizeFactory.create(name="16").id,
        "description": "Troca de roupas e sapatos",
        "child_id": child.id
    }

    url = reverse('gen_swaps')
    client.force_authenticate(user=ben.user)
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.data['status']['name'] == PENDING


@pytest.mark.django_db
def test_vol_can_create_swap(client: APIClient):
    StatusFactory.create(name=APPROVED)
    ben = make_beneficiary()
    child = make_less_than_one_year_child(beneficiary=ben)

    data = {
        "cloth_size_id": SizeFactory.create(name="RN").id,
        "shoe_size_id": SizeFactory.create(name="16").id,
        "description": "Troca de roupas e sapatos",
        "child_id": child.id
    }

    url = reverse('gen_swaps')

    client.force_authenticate(user=make_volunteer([MANAGE_SWAPS]).user)
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['message'] == "Beneficiária não especificada"

    data['beneficiary_id'] = ben.id
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.data['status']['name'] == APPROVED


@pytest.mark.django_db
def test_cannot_create_swap_for_another_beneficiary_child(client: APIClient):
    StatusFactory.create(name=PENDING)
    ben1 = make_beneficiary()
    
    ben = make_beneficiary()
    children = ChildFactory.create_batch(2, beneficiary=ben)

    data = {
        "cloth_size_id": SizeFactory.create(name="RN").id,
        "shoe_size_id": SizeFactory.create(name="16").id,
        "description": "Troca de roupas e sapatos",
        "child_id": children[1].id
    }

    url = reverse('gen_swaps')
    client.force_authenticate(user=ben1.user)
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['message'] == "A criança não pertence à beneficiária"


@pytest.mark.django_db
def test_cannot_create_more_than_one_swap_per_ben(client: APIClient):
    StatusFactory.create(name=PENDING)
    ben = make_beneficiary()
    child = make_less_than_one_year_child(beneficiary=ben)

    data = {
        "cloth_size_id": SizeFactory.create(name="RN").id,
        "shoe_size_id": SizeFactory.create(name="16").id,
        "description": "Troca de roupas e sapatos",
        "child_id": child.id
    }

    url = reverse('gen_swaps')
    client.force_authenticate(user=ben.user)
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['message'] == "Beneficiária já possui uma troca pendente"
