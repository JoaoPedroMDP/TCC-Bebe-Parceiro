#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import MaritalStatusFactory


@pytest.mark.django_db
def test_can_list_all_marital_statuses(client):
    marital_statuses = MaritalStatusFactory.create_batch(size=10)

    url = reverse("gen_marital_statuses")
    response = client.get(url)
    assert len(response.data) == len(marital_statuses)
