#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_CAMPAIGNS
from factories import CampaignFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_get_campaign(client: APIClient):
    campaign = CampaignFactory.create(name="TCGCa")
    url = reverse("spe_campaigns", kwargs={"pk": campaign.id})

    response = client.get(url)

    assert response.status_code == 200
    assert response.data["name"] == campaign.name
