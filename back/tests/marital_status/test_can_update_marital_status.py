#  coding: utf-8

from django.urls import reverse
from rest_framework.test import APIClient

from core.models import MaritalStatus
from factories import MaritalStatusFactory


def test_can_update_marital_status(client: APIClient):
    marital_status: MaritalStatus = MaritalStatusFactory.create()
    url = reverse("spe_marital_statuses", kwargs={"pk": marital_status.id})
    data = {"name": "TCUMS"}
    response = client.patch(url, data=data)

    assert response.status_code == 200
    assert response.data["name"] == data["name"]
