#  coding: utf-8
import logging
from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import MANAGE_SWAPS
from factories import SwapFactory
from tests.conftest import make_beneficiary_with_children, make_volunteer


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_vol_can_update_swap(client: APIClient):
    ben, children = make_beneficiary_with_children()
    swap = SwapFactory.create(beneficiary=ben, child=children[0])

    vol = make_volunteer([MANAGE_SWAPS])
    url = reverse('spe_swaps', kwargs={'pk': swap.id})
    swap_data = swap.to_dict()
    swap_data['description'] = 'Nova descrição, atualizada'
    swap_data['child_id'] = children[1].id

    client.force_authenticate(vol.user)
    response = client.patch(url, swap_data)

    assert response.status_code == 200
    assert response.data['description'] == 'Nova descrição, atualizada'
    assert response.data['child']['id'] == children[1].id
