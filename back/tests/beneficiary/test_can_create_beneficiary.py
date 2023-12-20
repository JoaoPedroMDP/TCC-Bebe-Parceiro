#  coding: utf-8
import pytest
from django.urls import reverse
from django.test.client import Client

from tests.utils.access_code_utils import create_access_code
from tests.utils.beneficiary_utils import default_beneficiary_data
from tests.utils.city_utils import create_city
from tests.utils.marital_status_utils import create_marital_status


@pytest.mark.django_db
def test_can_create_beneficiary(client: Client):
    marital_status = create_marital_status()
    city = create_city()
    access_code = create_access_code()

    data = default_beneficiary_data(marital_status.id, city.id, access_code.code)
    url = reverse('gen_beneficiaries')
    response = client.post(url, data=data, content_type='application/json')

    assert response.status_code == 201
    assert response.data['user']['name'].startswith(data["name"]) is True

    # TODO: Terminar