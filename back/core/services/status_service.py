#  coding: utf-8
from typing import List

from core.cqrs.queries.status_queries import GetStatusQuery, ListStatusQuery
from core.models import Status
from core.repositories.status_repository import StatusRepository
from core.services import CrudService


class StatusService(CrudService):
    @classmethod
    def filter(cls, query: ListStatusQuery) -> List[Status]:
        return StatusRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetStatusQuery) -> Status:
        return StatusRepository.get(query.id)
