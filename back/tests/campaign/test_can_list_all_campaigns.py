#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_CAMPAIGNS
from factories import CampaignFactory
from tests.conftest import make_user

lgr = logging.getLogger(__name__)

@pytest.mark.django_db
def test_can_list_all_campaigns(client: APIClient):
    campaigns = CampaignFactory.create_batch(size=5)
    url = reverse("gen_campaigns")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(campaigns)
