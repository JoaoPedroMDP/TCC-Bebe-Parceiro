#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_VOLUNTEERS
from factories import VolunteerFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_list_all_volunteers(client: APIClient):
    volunteers = VolunteerFactory.create_batch(size=10)

    url = reverse("gen_volunteers")

    # Sem autenticação
    response = client.get(url)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_VOLUNTEERS]))
    response = client.get(url)
    print(response.data)
    assert len(response.data) == len(volunteers)
