#  coding: utf-8
from typing import List

from core.cqrs.commands.register_commands import CreateRegisterCommand, PatchRegisterCommand, \
    DeleteRegisterCommand
from core.cqrs.queries.register_queries import GetRegisterQuery, ListRegisterQuery
from core.models import Register
from core.repositories.register_repository import RegisterRepository
from core.services import CrudService


class RegisterService(CrudService):
    @classmethod
    def create(cls, command: CreateRegisterCommand) -> Register:
        new_register = RegisterRepository.create(command.to_dict())
        return new_register

    @classmethod
    def patch(cls, command: PatchRegisterCommand) -> Register:
        return RegisterRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListRegisterQuery) -> List[Register]:
        return RegisterRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetRegisterQuery) -> Register:
        return RegisterRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteRegisterCommand) -> bool:
        return RegisterRepository.delete(command.id)
