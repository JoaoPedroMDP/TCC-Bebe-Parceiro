
from datetime import datetime, timedelta
from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_REPORTS
from factories import VolunteerFactory
from tests.conftest import make_volunteer


def prepare_days(base_date: datetime):
    yesterday = VolunteerFactory.create_batch(3)
    before_yesterday = VolunteerFactory.create_batch(2)
    three_days_ago = VolunteerFactory.create_batch(1)

    for x in yesterday:
        x.created_at = base_date - timedelta(days=1)
        x.save()
        
    for x in before_yesterday:
        x.created_at = base_date - timedelta(days=2)
        x.save()

    for x in three_days_ago:
        x.created_at = base_date - timedelta(days=3)
        x.save()


@pytest.mark.django_db
def test_volunteer_report(client: APIClient):
    now = datetime.now()
    prepare_days(now)

    data = {
        "start_date": (now - timedelta(days=2)).strftime('%Y-%m-%d'),
        "end_date": (now - timedelta(days=1)).strftime('%Y-%m-%d')
    }

    url = reverse('reports_volunteers')

    vol = make_volunteer([MANAGE_REPORTS])
    client.force_authenticate(vol.user)

    response = client.get(url, data)
    assert response.status_code == 200
    assert len(response.json()) == 5
