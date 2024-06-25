#  coding: utf-8
from datetime import datetime, time, timedelta
from typing import List

import pytest
from django.contrib.auth.models import Group
from rest_framework.test import APIClient

from config import GROUPS
from core.models import User
from factories import BeneficiaryFactory, ChildFactory, CityFactory, GroupFactory, UserFactory, VolunteerFactory


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['pt_BR']


@pytest.fixture(scope='function', autouse=True)
def faker_seed():
    return time().microsecond


@pytest.fixture(autouse=True)
def seed_db(db):
    for g in GROUPS:
        GroupFactory.create(name=g)


@pytest.fixture
def client():
    return APIClient()


def make_user(u_permissions: List[str] = []) -> User:
    groups = Group.objects.filter(name__in=u_permissions)
    user: User = UserFactory.create()
    user.groups.add(*groups)
    return user


def make_volunteer(roles: List[str] = []):
    v_user = make_user(roles)
    vol = VolunteerFactory.create(user=v_user)
    return vol


def make_beneficiary(**kwargs):
    b_user = make_user()
    ben = BeneficiaryFactory.create(user=b_user, **kwargs)
    return ben


def make_beneficiary_with_children(**kwargs):
    ben = make_beneficiary(**kwargs)
    children = ChildFactory.create_batch(2, beneficiary=ben)
    return ben, children


def make_child(**kwargs):
    child = ChildFactory.create(**kwargs)
    return child


def make_less_than_one_year_child(**kwargs):
    today = datetime.today()
    birth_date = today - timedelta(days=365)
    child = ChildFactory.create(birth_date=birth_date, **kwargs)
    return child


def make_city(**kwargs):
    return CityFactory.create(**kwargs)