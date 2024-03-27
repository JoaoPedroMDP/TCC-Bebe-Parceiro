#  coding: utf-8
from typing import List

import pytest
from django.contrib.auth.models import Group
from django.test.client import Client
from django.urls import reverse

from core.models import User, City
from factories import UserFactory, CityFactory, GroupFactory


@pytest.mark.django_db
def test_can_create_volunteer(client: Client):
    url = reverse('gen_volunteers')
    user: User = UserFactory.build()
    city: City = CityFactory.create()
    groups: List[Group] = GroupFactory.create_batch(3)

    data = {
        "name": user.name,
        "phone": user.phone,
        "email": user.email,
        "password": user.password,
        "city_id": city.id,
        "group_ids": [group.id for group in groups],
    }
    response = client.post(url, data=data, content_type='application/json')

    assert response.status_code == 201
    assert response.data['user']['name'] == user.name
    assert response.data['user']['email'] == user.email
    assert response.data['city']['id'] == city.id

    for g in [g.name for g in groups]:
        found = False
        for gr in response.data['user']['groups']:
            if g == gr['name']:
                found = True
                break

        assert found
