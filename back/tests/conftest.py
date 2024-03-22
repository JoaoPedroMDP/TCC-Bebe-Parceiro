#  coding: utf-8
from datetime import time

import pytest

from config import GROUPS, ROLES
from factories import GroupFactory


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
