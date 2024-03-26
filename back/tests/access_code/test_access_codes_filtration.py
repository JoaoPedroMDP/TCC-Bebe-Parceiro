#  coding: utf-8
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from config import MANAGE_ACCESS_CODES
from factories import AccessCodeFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_access_codes_by_prefix(client: APIClient):
    AccessCodeFactory.create_batch(size=5)
    code_to_filter = AccessCodeFactory.create()
    data = {"code": code_to_filter.code}
    url = reverse("gen_access_codes")

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ACCESS_CODES]))
    response = client.get(url, data=data)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["code"] == code_to_filter.code


@pytest.mark.django_db
def test_can_filter_access_codes_by_used(client: APIClient):
    AccessCodeFactory.create_batch(size=5, used=True)
    AccessCodeFactory.create_batch(size=3, used=False)
    data = {"used": True}
    url = reverse("gen_access_codes")

    # Sem autenticação
    response = client.get(url, data=data)
    assert response.status_code == 401

    # Com autenticação
    client.force_authenticate(make_user([MANAGE_ACCESS_CODES]))
    response = client.get(url, data=data)
    assert response.status_code == 200
    assert len(response.data) == 5
