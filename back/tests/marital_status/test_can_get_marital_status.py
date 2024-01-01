#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import MaritalStatusFactory


@pytest.mark.django_db
def test_can_get_marital_status(client: Client):
    marital_status = MaritalStatusFactory.create()
    url = reverse("spe_marital_statuses", kwargs={"pk": marital_status.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == marital_status.name
