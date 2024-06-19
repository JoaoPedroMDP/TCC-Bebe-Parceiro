#  coding: utf-8
import logging
from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_CAMPAIGNS
from factories import CampaignFactory
from tests.conftest import make_volunteer


lgr = logging.getLogger(__name__)
@pytest.mark.django_db
def test_can_update_campaign(client: APIClient):
    campaign = CampaignFactory.create()
    data = campaign.to_dict()
    lgr.debug(data)
    data['description'] = 'Nova descrição'

    url = reverse("spe_campaigns", kwargs={"pk": campaign.id})

    # Sem autenticação
    response = client.patch(url, data)
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_CAMPAIGNS])
    client.force_authenticate(vol.user)
    
    response = client.patch(url, data)
    assert response.status_code == 200
    assert response.data['description'] == 'Nova descrição'
