#  coding: utf-8
from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from config import FINISHED, MANAGE_SWAPS, PENDING
from factories import StatusFactory, SwapFactory
from tests.conftest import make_beneficiary_with_children, make_user, make_volunteer


@pytest.mark.django_db
def test_vol_can_list_all_swaps(client: APIClient):
    ben, children = make_beneficiary_with_children()
    SwapFactory.create_batch(3, beneficiary=ben, child=children[0])
    
    url = reverse('gen_swaps')
    vol = make_volunteer([MANAGE_SWAPS])
    client.force_authenticate(vol.user)

    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_ben_can_see_only_its_swaps(client: APIClient):
    ben1, children1 = make_beneficiary_with_children()
    SwapFactory.create_batch(3, beneficiary=ben1, child=children1[0])
    
    ben2, children2 = make_beneficiary_with_children()
    SwapFactory.create_batch(2, beneficiary=ben2, child=children2[0])

    url = reverse('gen_swaps')
    client.force_authenticate(ben2.user)

    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_can_filter_swap_by_status(client: APIClient):
    ben, children = make_beneficiary_with_children()
    fin = StatusFactory.create(name=FINISHED)
    pen = StatusFactory.create(name=PENDING)
    SwapFactory.create_batch(3, beneficiary=ben, child=children[0], status=pen)
    
    url = reverse('gen_swaps')
    vol = make_volunteer([MANAGE_SWAPS])
    client.force_authenticate(vol.user)

    response = client.get(url, {'status_id': pen.id})
    assert response.status_code == 200
    assert len(response.data) == 3

    response = client.get(url, {'status_id': fin.id})
    assert response.status_code == 200
    assert len(response.data) == 0
