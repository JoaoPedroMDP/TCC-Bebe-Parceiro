#  coding: utf-8
import logging

from core.models import MaritalStatus
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class MaritalStatusRepository(Repository):
    model = MaritalStatus

    @classmethod
    def list(cls, filters: dict):
        return super().list(**filters)
