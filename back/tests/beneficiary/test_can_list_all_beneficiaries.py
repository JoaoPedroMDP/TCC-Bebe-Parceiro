#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import BeneficiaryFactory


@pytest.mark.django_db
def test_can_list_all_beneficiaries(client: Client):
    beneficiaries = BeneficiaryFactory.create_batch(size=10)

    url = reverse("gen_beneficiaries")
    response = client.get(url)
    assert len(response.data) == len(beneficiaries)
