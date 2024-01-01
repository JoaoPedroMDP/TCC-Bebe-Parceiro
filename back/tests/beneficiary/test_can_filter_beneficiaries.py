#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import BeneficiaryFactory


@pytest.mark.django_db
def test_can_filter_beneficiaries(client: Client):
    BeneficiaryFactory.create_batch(10, child_count=2)

    beneficiary = BeneficiaryFactory.create(child_count=1)

    url = reverse("gen_beneficiaries")
    data = {"child_count": beneficiary.child_count}
    response = client.get(url, data=data, content_type='application/json')

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['child_count'] == beneficiary.child_count

    data = {"user_id": beneficiary.user.id}
    response = client.get(url, data=data, content_type='application/json')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['user']['id'] == beneficiary.user.id
