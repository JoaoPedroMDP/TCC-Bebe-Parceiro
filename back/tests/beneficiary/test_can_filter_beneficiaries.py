#  coding: utf-8
import pytest

from tests.utils.beneficiary_utils import default_beneficiary_data


@pytest.mark.django_db
def test_can_filter_beneficiaries(client):
    beneficiary_data = default_beneficiary_data()

