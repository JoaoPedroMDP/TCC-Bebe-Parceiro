#  coding: utf-8
from datetime import time
from typing import List

import pytest
from django.contrib.auth.models import Group
from rest_framework.test import APIClient

from config import GROUPS, ROLE_BENEFICIARY, ROLE_VOLUNTEER, ROLES
from core.models import User
from factories import BeneficiaryFactory, ChildFactory, GroupFactory, UserFactory, VolunteerFactory


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

    for r in ROLES:
        GroupFactory.create(name=r)


@pytest.fixture
def client():
    return APIClient()


def make_user(u_permissions: List[str]) -> User:
    groups = Group.objects.filter(name__in=u_permissions)
    user: User = UserFactory.create()
    user.groups.add(*groups)
    return user


def make_beneficiary_with_children():
    b_user = make_user([ROLE_BENEFICIARY])
    ben = BeneficiaryFactory.create(user=b_user)
    children = ChildFactory.create_batch(2, beneficiary=ben)
    return ben, children


def make_volunteer(roles: List[str]):
    v_user = make_user([ROLE_VOLUNTEER, *roles])
    vol = VolunteerFactory.create(user=v_user)
    return vol
