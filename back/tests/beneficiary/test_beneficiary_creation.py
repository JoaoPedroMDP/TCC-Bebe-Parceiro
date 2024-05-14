#  coding: utf-8
import json
import logging

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_BENEFICIARIES
from factories import CityFactory, AccessCodeFactory, MaritalStatusFactory
from tests.conftest import make_user


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_create_beneficiary(client: APIClient):
    marital_status = MaritalStatusFactory.create()
    city = CityFactory.create()
    access_code = AccessCodeFactory.create(used=False)

    data = {
        "name": "TCCB",
        "birth_date": "2023-01-01",
        "child_count": 3,
        "email": "TCCB@email.com",
        "has_disablement": True,
        "marital_status_id": marital_status.id,
        "monthly_familiar_income": 1234,
        "password": "123456",
        "phone": "4495263859",
        "city_id": city.id,
        "access_code": access_code.code,
        "social_programs": [],
        "children": [
            {
                "name": "João ",
                "birth_date": "2023-01-01",
                "sex": "Masculino"
            },
            {
                "name": "Maria",
                "birth_date": "2023-02-02",
                "sex": "Feminino"
            }
        ]
    }

    url = reverse('gen_beneficiaries')
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 201
    assert response.data['user']['name'].startswith(data["name"]) is True

    # Agora, se for uma voluntária com permissão de gerenciar beneficiadas, não precisa de código de acesso
    url = reverse('create_beneficiaries')
    client.force_authenticate(make_user([MANAGE_BENEFICIARIES]))
    data.pop("access_code")
    data['email'] += '2'
    data['phone'] += '2'
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.data['user']['name'].startswith(data["name"]) is True

