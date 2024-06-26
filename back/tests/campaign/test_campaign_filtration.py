#  coding: utf-8
from datetime import date
import logging
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_CAMPAIGNS
from factories import CampaignFactory
from tests.conftest import make_volunteer


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_filter_campaigns_by_name(client: APIClient):
    CampaignFactory.create_batch(size=5)
    campaign_to_filter = CampaignFactory.create(name="CAMPANHA TESTE")
    data = {"name": campaign_to_filter.name}

    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)

    url = reverse("gen_campaigns")
    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == campaign_to_filter.name


@pytest.mark.django_db
def test_can_get_open_campaigns(client: APIClient):
    open_start = date.today()
    open_end = open_start.replace(month=open_start.month + 1)
    close_start = open_start.replace(month=open_start.month - 2)
    close_end = open_start.replace(month=open_start.month - 1)

    CampaignFactory.create_batch(size=2, start_date=open_start, end_date=open_end)
    CampaignFactory.create_batch(size=2, start_date=close_start, end_date=close_end)

    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)
    
    url = reverse("open_campaigns")
    response = client.get(url)
    
    assert len(response.data) == 2


@pytest.mark.django_db
def test_can_list_all_campaigns(client: APIClient):
    campaigns = CampaignFactory.create_batch(size=5)
    
    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)

    url = reverse("gen_campaigns")
    response = client.get(url)
    
    assert response.status_code == 200
    assert len(response.data) == len(campaigns)
