#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from factories import MaritalStatusFactory

lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_filter_marital_statuses_by_enabled(client: APIClient):
    MaritalStatusFactory.create_batch(size=5, enabled=False)
    MaritalStatusFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_marital_statuses")
    data = {"enabled": True}

    # Sem autenticação
    response = client.get(url, data=data)
    assert len(response.data) == 3


@pytest.mark.django_db
def test_can_filter_marital_statuses_by_name(client: APIClient):
    MaritalStatusFactory.create_batch(size=5)
    marital_status_to_filter = MaritalStatusFactory.create(name="TESTE")
    url = reverse("gen_marital_statuses")
    data = {"name": marital_status_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == marital_status_to_filter.name
