
from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import FINISHED, PENDING
from core.models import Status, Swap
from factories import StatusFactory, SwapFactory
from tests.conftest import make_beneficiary_with_children


@pytest.mark.django_db
def test_can_check_if_beneficiary_can_request_swap(client: APIClient):
    pending: Status = StatusFactory.create(name=PENDING)
    finished: Status = StatusFactory.create(name=FINISHED)
    ben, children = make_beneficiary_with_children()
    swap: Swap = SwapFactory.create(child=children[0], beneficiary=ben, status=pending)

    url = reverse('can_request_swap_beneficiaries')
    client.force_authenticate(ben.user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['can_request_swap'] is False

    swap.status = finished
    swap.save()

    response = client.get(url)
    assert response.status_code == 200
    assert response.data['can_request_swap'] is True
