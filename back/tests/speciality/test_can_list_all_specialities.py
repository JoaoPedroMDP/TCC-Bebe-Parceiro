#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_SPECIALITIES
from factories import SpecialityFactory
from tests.conftest import make_user

lgr = logging.getLogger(__name__)

@pytest.mark.django_db
def test_can_list_all_specialities(client: APIClient):
    countries = SpecialityFactory.create_batch(size=5)
    client.force_authenticate(make_user([MANAGE_SPECIALITIES]))

    url = reverse("gen_specialities")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(countries)
