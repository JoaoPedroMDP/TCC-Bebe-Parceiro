#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import BeneficiaryFactory, CityFactory, MaritalStatusFactory


@pytest.mark.django_db
def test_can_get_beneficiary(client: Client):
    city = CityFactory.create()
    marital = MaritalStatusFactory.create()

    beneficiary = BeneficiaryFactory.create(city=city, marital_status=marital)
    url = reverse("spe_beneficiaries", kwargs={"pk": beneficiary.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["user"]["name"] == beneficiary.user.name
