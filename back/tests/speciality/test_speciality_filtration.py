#  coding: utf-8
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config import MANAGE_SPECIALITIES
from factories import SpecialityFactory
from tests.conftest import make_user


@pytest.mark.django_db
def test_can_filter_countries_by_enabled(client: APIClient):
    SpecialityFactory.create_batch(size=5, enabled=False)
    SpecialityFactory.create_batch(size=3, enabled=True)

    url = reverse("gen_specialities")
    data = {"enabled": True}

    response = client.get(url, data=data)
    assert len(response.data) == 3


@pytest.mark.django_db
def test_can_filter_specialities_by_name(client: APIClient):
    SpecialityFactory.create_batch(size=5)
    speciality_to_filter = SpecialityFactory.create(name="TESTE")

    url = reverse("gen_specialities")
    data = {"name": speciality_to_filter.name}

    response = client.get(url, data=data)
    assert len(response.data) == 1
    assert response.data[0]["name"] == speciality_to_filter.name

