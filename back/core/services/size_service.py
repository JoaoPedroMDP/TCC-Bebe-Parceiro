#  coding: utf-8
from typing import List

from core.cqrs.commands.size_commands import CreateSizeCommand, PatchSizeCommand, \
    DeleteSizeCommand
from core.cqrs.queries.size_queries import GetSizeQuery, ListSizeQuery
from core.models import Size
from core.repositories.size_repository import SizeRepository
from core.services import CrudService


class SizeService(CrudService):
    @classmethod
    def create(cls, command: CreateSizeCommand) -> Size:
        new_size = SizeRepository.create(command.to_dict())
        return new_size

    @classmethod
    def patch(cls, command: PatchSizeCommand) -> Size:
        return SizeRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListSizeQuery) -> List[Size]:
        return SizeRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetSizeQuery) -> Size:
        return SizeRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteSizeCommand) -> bool:
        return SizeRepository.delete(command.id)
