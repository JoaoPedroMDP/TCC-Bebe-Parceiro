#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from factories import UserFactory


@pytest.mark.django_db
def test_can_login(client: Client):
    password = "testesenha"
    user = UserFactory.create(password=password)

    url = reverse('login')
    response = client.post(url, {
        "username": user.username,
        "password": password
    })

    assert response.status_code == 200
    assert 'token' in response.data
    assert 'expiry' in response.data
