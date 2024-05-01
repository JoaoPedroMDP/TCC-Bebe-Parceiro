#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from factories import CampaignFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_campaigns_by_name(client: APIClient):
    CampaignFactory.create_batch(size=5)
    campaign_to_filter = CampaignFactory.create(name="CAMPANHA TESTE")

    url = reverse("gen_campaigns")
    data = {"name": campaign_to_filter.name}

    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == campaign_to_filter.name

