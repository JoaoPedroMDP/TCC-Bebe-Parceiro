#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import AccessCodeFactory


@pytest.mark.django_db
def test_can_check_access_code(client: Client):
    used_code = AccessCodeFactory.create(used=True)
    unused_code = AccessCodeFactory.create(used=False)
    random_code = "random_code"

    url = reverse("check_access_code")
    response = client.get(url, data={"code": unused_code.code})
    assert response.status_code == 200

    response = client.get(url, data={"code": used_code.code})
    assert response.status_code == 403

    response = client.get(url, data={"code": random_code})
    assert response.status_code == 404
