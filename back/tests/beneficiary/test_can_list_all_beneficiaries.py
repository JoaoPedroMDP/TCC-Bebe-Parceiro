#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import BeneficiaryFactory, CityFactory, MaritalStatusFactory


@pytest.mark.django_db
def test_can_list_all_beneficiaries(client: Client):
    city = CityFactory.create()
    marital = MaritalStatusFactory.create()

    beneficiaries = BeneficiaryFactory.create_batch(size=10, city=city, marital_status=marital)

    url = reverse("gen_beneficiaries")
    response = client.get(url)
    assert len(response.data) == len(beneficiaries)
