#  coding: utf-8
from typing import List

from core.cqrs.commands.speciality_commands import CreateSpecialityCommand, PatchSpecialityCommand, \
    DeleteSpecialityCommand
from core.cqrs.queries.speciality_queries import GetSpecialityQuery, ListSpecialityQuery
from core.models import Speciality
from core.repositories.speciality_repository import SpecialityRepository
from core.services import CrudService
from core.utils.exceptions import HttpFriendlyException

class SpecialityService(CrudService):
    @classmethod
    def create(cls, command: CreateSpecialityCommand) -> Speciality:
        new_speciality = SpecialityRepository.create(command.to_dict())
        return new_speciality

    @classmethod
    def patch(cls, command: PatchSpecialityCommand) -> Speciality:
        return SpecialityRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListSpecialityQuery) -> List[Speciality]:
        return SpecialityRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetSpecialityQuery) -> Speciality:
        return SpecialityRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteSpecialityCommand) -> bool:
        speciality: Speciality = SpecialityRepository.get(command.id)
        if speciality.professionals.count() > 0:
            raise HttpFriendlyException("Não é possível deletar uma especialidade que possui profissionais associados.")

        return SpecialityRepository.delete(command.id)
