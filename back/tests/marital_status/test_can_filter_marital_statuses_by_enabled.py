#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import MaritalStatusFactory


@pytest.mark.django_db
def test_can_filter_marital_statuses_by_enabled(client):
    MaritalStatusFactory.create_batch(size=5, enabled=False)
    MaritalStatusFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_marital_statuses")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
