#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.country_utils import create_country


@pytest.mark.django_db
def test_can_create_state(client):
    test_country = create_country(name="TC")

    data = {'name': "TCCC", "country_id": test_country.id}
    url = reverse('gen_states')
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
