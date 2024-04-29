#  coding: utf-8

from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_MARITAL_STATUSES
from core.models import MaritalStatus
from factories import MaritalStatusFactory
from tests.conftest import make_user


def test_can_update_marital_status(client: APIClient):
    marital_status: MaritalStatus = MaritalStatusFactory.create()
    url = reverse("spe_marital_statuses", kwargs={"pk": marital_status.id})
    data = {"name": "TCUMS"}
    # Sem autenticação
    response = client.patch(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_MARITAL_STATUSES]))
    response = client.patch(url, data=data)

    assert response.status_code == 200
    assert response.data["name"] == data["name"]
