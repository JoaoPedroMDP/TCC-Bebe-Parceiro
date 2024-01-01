#  coding: utf-8
from typing import List

from core.cqrs.commands.country_commands import CreateCountryCommand, PatchCountryCommand, \
    DeleteCountryCommand
from core.cqrs.queries.country_queries import GetCountryQuery, ListCountryQuery
from core.models import Country
from core.repositories.country_repository import CountryRepository
from core.services import CrudService


class CountryService(CrudService):
    @classmethod
    def create(cls, command: CreateCountryCommand) -> Country:
        new_country = CountryRepository.create(command.to_dict())
        return new_country

    @classmethod
    def patch(cls, command: PatchCountryCommand) -> Country:
        return CountryRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListCountryQuery) -> List[Country]:
        return CountryRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetCountryQuery) -> Country:
        return CountryRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteCountryCommand) -> bool:
        return CountryRepository.delete(command.id)
