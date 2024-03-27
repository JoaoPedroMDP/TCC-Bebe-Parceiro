#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from core.repositories.group_repository import GroupRepository
from factories import UserFactory, BeneficiaryFactory, CityFactory, MaritalStatusFactory, VolunteerFactory


def beneficiary(password: str, client: Client, url: str):
    b_user = UserFactory.create(password=password)
    city = CityFactory.create()
    marital_status = MaritalStatusFactory.create()
    BeneficiaryFactory.create(user=b_user, city=city, marital_status=marital_status)
    response = client.post(url, {
        "username": b_user.username,
        "password": password
    })

    assert response.status_code == 200
    assert 'token' in response.data
    assert 'expiry' in response.data
    assert 'role' in response.data['user']
    assert response.data['user']['role'] == 'beneficiary'
    assert 'password' not in response.data['user']
    assert response.data['user']['id'] == b_user.id


def volunteer(password: str, client: Client, url: str):
    group = list(GroupRepository.filter(name='role_volunteer'))[0]
    v_user = UserFactory.create(password=password)
    v_user.groups.add(group)
    city = CityFactory.create()
    VolunteerFactory.create(user=v_user, city=city)
    response = client.post(url, {
        "username": v_user.username,
        "password": password
    })

    assert response.status_code == 200
    assert 'token' in response.data
    assert 'expiry' in response.data
    assert 'role' in response.data['user']
    assert response.data['user']['role'] == 'volunteer'
    assert 'password' not in response.data['user']
    assert response.data['user']['id'] == v_user.id


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
    assert 'role' in response.data['user']
    assert 'password' not in response.data['user']
    assert response.data['user']['id'] == user.id

    beneficiary(password, client, url)
    volunteer(password, client, url)
