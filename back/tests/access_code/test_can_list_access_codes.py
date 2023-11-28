#  coding: utf-8
import pytest

from tests.utils.access_code_utils import create_access_code


@pytest.mark.django_db
def test_can_list_access_codes(client):
    response = create_access_code(client, prefix="TCLAC")

    assert response.status_code == 201
    assert response.data['code'].startswith("TCLAC") is True
    assert response.data['used'] is False
