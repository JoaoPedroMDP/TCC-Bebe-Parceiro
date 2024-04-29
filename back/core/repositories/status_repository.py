#  coding: utf-8
from core.models import Status
from core.repositories import Repository


class StatusRepository(Repository):
    model = Status
