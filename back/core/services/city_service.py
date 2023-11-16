#  coding: utf-8
from typing import List

from core.cqrs.commands.city_commands import CreateCityCommand, PatchCityCommand, \
    DeleteCityCommand
from core.cqrs.queries.city_queries import GetCityQuery, ListCityQuery
from core.db_models.adress_related_models import City
from core.repositories.city_repository import CityRepository
from core.services import Service


class CityService(Service):
    @classmethod
    def create(cls, command: CreateCityCommand) -> City:
        new_City = CityRepository.create(command.to_dict())
        return new_City

    @classmethod
    def patch(cls, command: PatchCityCommand) -> City:
        return CityRepository.patch(command.to_dict())

    @classmethod
    def list(cls, query: ListCityQuery) -> List[City]:
        return CityRepository.list(**query.to_dict())

    @classmethod
    def get(cls, query: GetCityQuery) -> City:
        return CityRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteCityCommand) -> bool:
        return CityRepository.delete(command.id)
