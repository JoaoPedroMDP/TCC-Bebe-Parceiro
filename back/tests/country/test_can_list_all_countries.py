#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ADDRESSES
from factories import CountryFactory
from tests.conftest import make_user

lgr = logging.getLogger(__name__)

@pytest.mark.django_db
def test_can_list_all_countries(client: APIClient):
    countries = CountryFactory.create_batch(size=5)
    client.force_authenticate(make_user([MANAGE_ADDRESSES]))

    url = reverse("gen_countries")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(countries)
