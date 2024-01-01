#  coding: utf-8
from typing import List

from core.cqrs.commands.state_commands import CreateStateCommand, PatchStateCommand, \
    DeleteStateCommand
from core.cqrs.queries.state_queries import GetStateQuery, ListStateQuery
from core.models import State
from core.repositories.country_repository import CountryRepository
from core.repositories.state_repository import StateRepository
from core.services import CrudService


class StateService(CrudService):
    @classmethod
    def create(cls, command: CreateStateCommand) -> State:
        # Verifica se o estado passado é válido
        CountryRepository.get(command.country_id)

        new_state = StateRepository.create(command.to_dict())
        return new_state

    @classmethod
    def patch(cls, command: PatchStateCommand) -> State:
        return StateRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListStateQuery) -> List[State]:
        return StateRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetStateQuery) -> State:
        return StateRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteStateCommand) -> bool:
        return StateRepository.delete(command.id)
