#  coding: utf-8
from datetime import datetime, timedelta
import json
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from factories import StatusFactory
from core.models import Volunteer
from config import APPROVED, MANAGE_EVALUATIONS, MANAGE_BENEFICIARIES, MANAGE_REGISTRATIONS
from tests.conftest import make_beneficiary, make_volunteer


@pytest.mark.django_db
def test_can_approve_beneficiary(client: APIClient):
    StatusFactory.create(name=APPROVED)
    ben = make_beneficiary(approved=False)
    vol: Volunteer = make_volunteer([MANAGE_REGISTRATIONS])
    evaluator: Volunteer = make_volunteer([MANAGE_EVALUATIONS])

    url = reverse("approve_beneficiaries", kwargs={"pk": ben.pk})
    client.force_authenticate(vol.user)

    # Sem avaliador nem data
    response = client.patch(url, content_type='application/json')
    assert response.status_code == 400

    # Com avaliador sem data
    params = {"volunteer_id": evaluator.id}
    response = client.patch(url, data=params, content_type='application/json')
    assert response.status_code == 400

    # Com avaliador e data
    params['datetime'] = (datetime.now() + timedelta(days=1)).isoformat()
    response = client.patch(url, data=json.dumps(params), content_type='application/json')
    assert response.status_code == 200 