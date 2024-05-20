#  coding: utf-8
import logging
from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_CAMPAIGNS
from factories import CampaignFactory
from tests.conftest import make_user


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
    client.force_authenticate(make_user([MANAGE_CAMPAIGNS]))
    response = client.patch(url, data)

    assert response.status_code == 200
    assert response.data['description'] == 'Nova descrição'
