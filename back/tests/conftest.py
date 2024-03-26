#  coding: utf-8
from datetime import time
from typing import List

import pytest
from django.contrib.auth.models import Group
from rest_framework.test import APIClient

from config import GROUPS, ROLES
from core.models import User
from factories import GroupFactory, UserFactory


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


def make_user(u_permissions: List[str]):
    groups = Group.objects.filter(name__in=u_permissions)
    user: User = UserFactory.create(username="user", password="user")
    user.groups.add(*groups)
    return user
