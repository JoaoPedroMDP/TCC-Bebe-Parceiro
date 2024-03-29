#  coding: utf-8
from typing import List

from core.cqrs.commands.city_commands import CreateCityCommand, PatchCityCommand, \
    DeleteCityCommand
from core.cqrs.queries.city_queries import GetCityQuery, ListCityQuery
from core.models import City
from core.repositories.city_repository import CityRepository
from core.repositories.state_repository import StateRepository
from core.services import CrudService


class CityService(CrudService):
    @classmethod
    def create(cls, command: CreateCityCommand) -> City:
        # Verifica se o estado passado é válido
        StateRepository.get(command.state_id)

        new_city = CityRepository.create(command.to_dict())
        return new_city

    @classmethod
    def patch(cls, command: PatchCityCommand) -> City:
        return CityRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListCityQuery) -> List[City]:
        return CityRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetCityQuery) -> City:
        return CityRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteCityCommand) -> bool:
        return CityRepository.delete(command.id)
