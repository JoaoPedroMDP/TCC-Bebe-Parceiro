#  coding: utf-8
import pytest
from django.test.client import Client
from django.urls import reverse

from core.repositories.group_repository import GroupRepository
from factories import UserFactory, BeneficiaryFactory, CityFactory, MaritalStatusFactory, VolunteerFactory




@pytest.mark.django_db
def test_volunteer_can_login(client: Client):
    password = "voluntaria"
    v_user = UserFactory.create(password=password)
    city = CityFactory.create()
    VolunteerFactory.create(user=v_user, city=city)

    url = reverse('login')

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
def test_beneficiary_can_login(client: Client):
    password = "beneficiaria"
    b_user = UserFactory.create(password=password)
    city = CityFactory.create()
    marital_status = MaritalStatusFactory.create()
    BeneficiaryFactory.create(user=b_user, city=city, marital_status=marital_status)

    url = reverse('login')

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
