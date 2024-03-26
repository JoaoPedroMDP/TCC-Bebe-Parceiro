#  coding: utf-8
import logging

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_ACCESS_CODES
from factories import AccessCodeFactory
from tests.conftest import make_user

lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_list_all_access_codes(client: APIClient):
    codes = AccessCodeFactory.create_batch(size=5)
    client.force_authenticate(make_user([MANAGE_ACCESS_CODES]))

    url = reverse("gen_access_codes")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == len(codes)
