#  coding: utf-8
from typing import List

from core.cqrs.commands.child_commands import CreateChildCommand, PatchChildCommand, \
    DeleteChildCommand
from core.cqrs.queries.child_queries import GetChildQuery, ListChildQuery
from core.repositories.child_repository import ChildRepository

from core.models import Child
from core.repositories.beneficiary_repository import BeneficiaryRepository
from core.services import CrudService


class ChildService(CrudService):
    @classmethod
    def create(cls, command: CreateChildCommand) -> Child:
        # Verifico se a beneficiada existe
        BeneficiaryRepository.get(command.beneficiary_id)

        new_child = ChildRepository.create(command.to_dict())
        return new_child

    @classmethod
    def patch(cls, command: PatchChildCommand) -> Child:
        return ChildRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListChildQuery) -> List[Child]:
        return ChildRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetChildQuery) -> Child:
        return ChildRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteChildCommand) -> bool:
        return ChildRepository.delete(command.id)
