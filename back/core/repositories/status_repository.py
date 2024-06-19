#  coding: utf-8
from core.models import Status
from core.repositories import Repository


class StatusRepository(Repository):
    model = Status

    @classmethod
    def get_by_name(cls, name: str):
        return cls.filter(name=name).get()
