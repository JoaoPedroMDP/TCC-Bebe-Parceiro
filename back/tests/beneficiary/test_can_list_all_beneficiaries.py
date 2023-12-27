#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.factories import BeneficiaryFactory


@pytest.mark.django_db
def test_can_list_all_beneficiaries(client):
    beneficiaries = BeneficiaryFactory.create_batch(size=10)

    url = reverse("gen_beneficiaries")
    response = client.get(url)
    assert len(response.data) == len(beneficiaries)
