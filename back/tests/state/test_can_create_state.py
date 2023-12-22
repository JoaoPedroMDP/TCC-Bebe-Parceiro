#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import CountryFactory


@pytest.mark.django_db
def test_can_create_state(client):
    test_country = CountryFactory.create(name="TC")

    data = {'name': "TCCS", "country_id": test_country.id}
    url = reverse('gen_states')
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'].startswith(data["name"]) is True
    assert response.data['enabled'] is True
