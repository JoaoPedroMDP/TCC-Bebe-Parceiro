#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from tests.utils.beneficiary_utils import default_beneficiary_data
from tests.utils.factories import CityFactory, AccessCodeFactory, MaritalStatusFactory


@pytest.mark.django_db
def test_can_create_beneficiary(client: Client):
    marital_status = MaritalStatusFactory.create()
    city = CityFactory.create()
    access_code = AccessCodeFactory.create(used=False)

    data = default_beneficiary_data(marital_status.id, city.id, access_code.code)
    url = reverse('gen_beneficiaries')
    response = client.post(url, data=data, content_type='application/json')

    # print(response)

    assert response.status_code == 201
    assert response.data['user']['name'].startswith(data["name"]) is True
