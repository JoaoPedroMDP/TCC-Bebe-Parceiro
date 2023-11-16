#  coding: utf-8
from typing import List

from core.cqrs.commands.state_commands import CreateStateCommand, PatchStateCommand, \
    DeleteStateCommand
from core.cqrs.queries.state_queries import GetStateQuery, ListStateQuery
from core.db_models.adress_related_models import State
from core.repositories.state_repository import StateRepository
from core.services import Service


class StateService(Service):
    @classmethod
    def create(cls, command: CreateStateCommand) -> State:
        new_State = StateRepository.create(command.to_dict())
        return new_State

    @classmethod
    def patch(cls, command: PatchStateCommand) -> State:
        return StateRepository.patch(command.to_dict())

    @classmethod
    def list(cls, query: ListStateQuery) -> List[State]:
        return StateRepository.list(**query.to_dict())

    @classmethod
    def get(cls, query: GetStateQuery) -> State:
        return StateRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteStateCommand) -> bool:
        return StateRepository.delete(command.id)
