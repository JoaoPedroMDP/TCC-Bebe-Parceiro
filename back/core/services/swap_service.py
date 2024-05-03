#  coding: utf-8
from typing import List

from core.cqrs.commands.swap_commands import CreateSwapCommand, PatchSwapCommand, \
    DeleteSwapCommand
from core.cqrs.queries.swap_queries import GetSwapQuery, ListSwapQuery
from core.models import Swap
from core.repositories.swap_repository import SwapRepository
from core.services import CrudService


class SwapService(CrudService):
    @classmethod
    def create(cls, command: CreateSwapCommand) -> Swap:
        return SwapRepository.create(command.to_dict())

    @classmethod
    def patch(cls, command: PatchSwapCommand) -> Swap:
        return SwapRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListSwapQuery) -> List[Swap]:
        filters = query.to_dict()
        if query.user.beneficiary:
            filters = {
                **filters, 
                "beneficiary_id": query.user.beneficiary.id
            }
        return SwapRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetSwapQuery) -> Swap:
        return SwapRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteSwapCommand) -> bool:
        return SwapRepository.delete(command.id)
