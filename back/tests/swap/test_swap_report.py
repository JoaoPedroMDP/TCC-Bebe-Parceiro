
from datetime import datetime, timedelta
from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_REPORTS
from factories import SwapFactory
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_swap_report(client: APIClient):
    SwapFactory.create_batch(3)
    now = datetime.now()

    data = {
        "start_date": (now - timedelta(days=1)).strftime('%Y-%m-%d'),
        "end_date": (now + timedelta(days=1)).strftime('%Y-%m-%d')
    }

    url = reverse('reports_swaps')

    vol = make_volunteer([MANAGE_REPORTS])
    client.force_authenticate(vol.user)

    response = client.get(url, data)
    assert response.status_code == 200
    assert len(response.json()) == 3
