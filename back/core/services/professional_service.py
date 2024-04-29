#  coding: utf-8
from typing import List

from core.cqrs.commands.professional_commands import (CreateProfessionalCommand, PatchProfessionalCommand,
                                                      DeleteProfessionalCommand)
from core.cqrs.queries.professional_queries import GetProfessionalQuery, ListProfessionalQuery
from core.models import Professional
from core.repositories.professional_repository import ProfessionalRepository
from core.services import CrudService


class ProfessionalService(CrudService):
    @classmethod
    def create(cls, command: CreateProfessionalCommand) -> Professional:
        new_professional = ProfessionalRepository.create(command.to_dict())
        return new_professional

    @classmethod
    def patch(cls, command: PatchProfessionalCommand) -> Professional:

        return ProfessionalRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListProfessionalQuery) -> List[Professional]:
        return ProfessionalRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetProfessionalQuery) -> Professional:
        return ProfessionalRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteProfessionalCommand) -> bool:
        return ProfessionalRepository.delete(command.id)
