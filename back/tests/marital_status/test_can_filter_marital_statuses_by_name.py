#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import MaritalStatusFactory


@pytest.mark.django_db
def test_can_filter_marital_statuses_by_name(client):
    MaritalStatusFactory.create_batch(size=5)
    marital_status_to_filter = MaritalStatusFactory.create(name="TESTE")
    url = reverse("gen_marital_statuses")
    data = {"name": marital_status_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == marital_status_to_filter.name

