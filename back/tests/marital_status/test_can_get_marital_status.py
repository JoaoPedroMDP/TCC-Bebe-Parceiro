#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.marital_status_utils import create_marital_status


@pytest.mark.django_db
def test_can_get_marital_status(client):
    marital_status = create_marital_status(name="TCGSP")
    url = reverse("spe_marital_statuses", kwargs={"pk": marital_status.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["name"] == marital_status.name
