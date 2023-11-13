#  coding: utf-8
from typing import List

from core.cqrs.commands.marital_status_commands import CreateMaritalStatusCommand, PatchMaritalStatusCommand, \
    DeleteMaritalStatusCommand
from core.cqrs.queries.marital_status_queries import GetMaritalStatusQuery, ListMaritalStatusQuery
from core.models import MaritalStatus
from core.repositories.marital_status_repository import MaritalStatusRepository
from core.services import Service


class MaritalStatusService(Service):
    @classmethod
    def create(cls, command: CreateMaritalStatusCommand) -> MaritalStatus:
        new_status = MaritalStatusRepository.create(command.to_dict())
        return new_status

    @classmethod
    def patch(cls, command: PatchMaritalStatusCommand) -> MaritalStatus:
        return MaritalStatusRepository.patch(command.to_dict())

    @classmethod
    def list(cls, query: ListMaritalStatusQuery) -> List[MaritalStatus]:
        return MaritalStatusRepository.list(query.to_dict())

    @classmethod
    def get(cls, query: GetMaritalStatusQuery) -> MaritalStatus:
        return MaritalStatusRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteMaritalStatusCommand) -> bool:
        return MaritalStatusRepository.delete(command.id)
