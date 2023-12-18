#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.marital_status_utils import create_n_marital_statuses, mark_marital_statuses_as_disabled


@pytest.mark.django_db
def test_can_filter_marital_statuses_by_enabled(client):
    enabled_marital_statuses = create_n_marital_statuses(name="TCFSPBE1", n=5)
    mark_marital_statuses_as_disabled(enabled_marital_statuses)
    create_n_marital_statuses(name="TCFSPBE2", n=3)

    url = reverse("gen_marital_statuses")
    data = {"enabled": True}
    response = client.get(url, data=data)
    assert len(response.data) == 3
