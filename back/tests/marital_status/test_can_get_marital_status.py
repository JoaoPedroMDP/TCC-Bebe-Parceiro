#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_MARITAL_STATUSES
from factories import MaritalStatusFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_get_marital_status(client: APIClient):
    marital_status = MaritalStatusFactory.create()
    url = reverse("spe_marital_statuses", kwargs={"pk": marital_status.id})

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_MARITAL_STATUSES]))
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["name"] == marital_status.name
