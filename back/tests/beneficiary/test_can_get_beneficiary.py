#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import BeneficiaryFactory


@pytest.mark.django_db
def test_can_get_beneficiary(client: Client):
    beneficiary = BeneficiaryFactory.create()
    url = reverse("spe_beneficiaries", kwargs={"pk": beneficiary.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["user"]["name"] == beneficiary.user.name
