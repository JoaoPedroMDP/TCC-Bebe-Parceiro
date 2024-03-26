#  coding: utf-8
from datetime import time

import pytest
from django.contrib.auth.models import Group

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


# @pytest.fixture()
# def ac_user(db):
#     group: Group = Group.objects.get(name='manage_access_codes')
#     user: User = UserFactory.create(username="ac_user", password="ac_user")
#     user.groups.add(group)
#     yield user
