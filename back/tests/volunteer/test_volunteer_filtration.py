#  coding: utf-8
from typing import List

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_VOLUNTEERS
from core.models import Volunteer
from factories import GroupFactory, VolunteerFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_volunteer_by_groups(client: APIClient):
    a_amount = 5
    b_amount = 3
    group_a = GroupFactory.create()
    group_b = GroupFactory.create()

    a_volunteers: List[Volunteer] = VolunteerFactory.create_batch(size=a_amount)
    b_volunteers: List[Volunteer] = VolunteerFactory.create_batch(size=b_amount)

    for a_vol in a_volunteers:
        a_vol.user.groups.add(group_a)

    for b_vol in b_volunteers:
        b_vol.user.groups.add(group_b)

    url = reverse("gen_volunteers")

    # Sem autenticação
    response = client.get(url, data={"group_ids": [group_a.id]})
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_VOLUNTEERS]))
    response = client.get(url, data={"group_ids": [group_a.id]})
    assert response.status_code == 200
    assert len(response.data) == a_amount

    response = client.get(url, data={"group_ids": [group_b.id]})
    assert response.status_code == 200
    assert len(response.data) == b_amount

    response = client.get(url, data={"group_ids": [group_a.id, group_b.id]})
    assert response.status_code == 200
    assert len(response.data) == a_amount + b_amount
