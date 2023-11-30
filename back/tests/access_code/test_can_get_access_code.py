#  coding: utf-8
import pytest
from django.urls import reverse

from tests.utils.access_code_utils import create_access_code


@pytest.mark.django_db
def test_can_get_access_code(client):
    ac = create_access_code(prefix="TCGAC")
    url = reverse("spe_access_codes", kwargs={"pk": ac.id})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["code"] == ac.code
