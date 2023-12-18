#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.marital_status_utils import create_n_marital_statuses


@pytest.mark.django_db
def test_can_filter_marital_statuses_by_name(client):
    marital_status_to_filter = create_n_marital_statuses(name="TCFSPBN", n=5)[2]

    url = reverse("gen_marital_statuses")
    data = {"name": marital_status_to_filter.name}
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == marital_status_to_filter.name

