from django.urls import reverse
from rest_framework.test import APIClient

import pytest

from config import MANAGE_REPORTS
from tests.conftest import make_beneficiary, make_volunteer


@pytest.mark.django_db
@pytest.mark.permissions
def test_appointment_report_permissions(client: APIClient):
    url = reverse('reports_appointments')

    # Anônimos não passam
    response = client.get(url)
    assert response.status_code == 401
    
    # Voluntárias sem permissão não passam
    vol = make_volunteer()
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 403

    # Beneficiárias não passam
    ben = make_beneficiary()
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 403

    # Voluntárias com permissão podem gerar relatórios
    vol = make_volunteer([MANAGE_REPORTS])
    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200
