#  coding: utf-8
from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import MANAGE_SWAPS
from factories import SwapFactory
from tests.conftest import make_beneficiary_with_children, make_volunteer


@pytest.mark.django_db
def test_vol_can_get_any_swap(client: APIClient):
    ben1, children1 = make_beneficiary_with_children()
    swap1 = SwapFactory(beneficiary=ben1, child=children1[0])

    ben2, children2 = make_beneficiary_with_children()
    swap2 = SwapFactory(beneficiary=ben2, child=children2[0])

    vol = make_volunteer([MANAGE_SWAPS])
    url = reverse('spe_swaps', kwargs={'pk': swap1.id})

    client.force_authenticate(vol.user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == swap1.id

    url = reverse('spe_swaps', kwargs={'pk': swap2.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == swap2.id
