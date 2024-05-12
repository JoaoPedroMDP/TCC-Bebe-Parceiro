#  coding: utf-8
from email.headerregistry import Group
from typing import List

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_VOLUNTEERS
from core.models import Volunteer
from factories import GroupFactory, VolunteerFactory
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_filter_volunteer_by_groups(client: APIClient):
    a_amount = 5
    b_amount = 3
    group_a: Group = GroupFactory.create()
    group_b: Group = GroupFactory.create()

    a_volunteers: List[Volunteer] = []
    for _ in range (a_amount):
        a_volunteers.append(make_volunteer([group_a.name]))

    b_volunteers: List[Volunteer] = []    
    for _ in range (b_amount):
        b_volunteers.append(make_volunteer([group_b.name]))

    url = reverse("gen_volunteers")

    # Sem autenticação
    response = client.get(url, data={"group_ids": [group_a.id]})
    assert response.status_code == 401

    # Com autenticação
    vol = make_volunteer([MANAGE_VOLUNTEERS])

    client.force_authenticate(vol.user)
    response = client.get(url, data={"group_ids": [group_a.id]})
    assert response.status_code == 200
    assert len(response.data) == a_amount

    response = client.get(url, data={"group_ids": [group_b.id]})
    assert response.status_code == 200
    assert len(response.data) == b_amount

    response = client.get(url, data={"group_ids": [group_a.id, group_b.id]})
    assert response.status_code == 200
    assert len(response.data) == a_amount + b_amount
