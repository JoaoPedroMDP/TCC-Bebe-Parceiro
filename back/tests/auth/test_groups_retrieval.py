#  coding: utf-8
from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from config import MANAGE_VOLUNTEERS
from django.contrib.auth.models import Group
from tests.conftest import make_volunteer


@pytest.mark.django_db
def test_can_list_all_groups(client: APIClient):
    vol = make_volunteer([MANAGE_VOLUNTEERS])

    all_groups = Group.objects.all()

    client.force_authenticate(user=vol.user)
    url = reverse('gen_groups')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(all_groups)
