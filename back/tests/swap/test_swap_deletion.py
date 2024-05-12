
from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_SWAPS
from core.models import Swap
from factories import SwapFactory
from tests.conftest import make_beneficiary_with_children, make_volunteer


@pytest.mark.django_db
def test_vol_can_delete_swap(client: APIClient):
    ben, children = make_beneficiary_with_children()
    swap = SwapFactory(beneficiary=ben, child=children[0])
    
    url = reverse('spe_swaps', kwargs={'pk': swap.id})
    vol = make_volunteer([MANAGE_SWAPS])
    client.force_authenticate(vol.user)

    response = client.delete(url)
    assert response.status_code == 204
    assert not Swap.objects.filter(id=swap.id).exists()


@pytest.mark.django_db
def test_ben_cannot_delete_swaps(client: APIClient):
    ben, children = make_beneficiary_with_children()
    swap = SwapFactory(beneficiary=ben, child=children[0])
    
    url = reverse('spe_swaps', kwargs={'pk': swap.id})
    client.force_authenticate(ben.user)

    response = client.delete(url)
    assert response.status_code == 403
    assert Swap.objects.filter(id=swap.id).exists()
