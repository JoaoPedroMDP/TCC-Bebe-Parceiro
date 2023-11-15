#  coding: utf-8
from typing import List

from core.cqrs.commands.benefited_commands import CreateBenefitedCommand, PatchBenefitedCommand, \
    DeleteBenefitedCommand
from core.cqrs.queries.benefited_queries import GetBenefitedQuery, ListBenefitedQuery
from core.models import Benefited
from core.repositories.benefited_repository import BenefitedRepository
from core.services import Service


class BenefitedService(Service):
    @classmethod
    def create(cls, command: CreateBenefitedCommand) -> Benefited:
        new_benefited = BenefitedRepository.create(command.to_dict())
        return new_benefited

    @classmethod
    def patch(cls, command: PatchBenefitedCommand) -> Benefited:
        return BenefitedRepository.patch(command.to_dict())

    @classmethod
    def list(cls, query: ListBenefitedQuery) -> List[Benefited]:
        return BenefitedRepository.list(**query.to_dict())

    @classmethod
    def get(cls, query: GetBenefitedQuery) -> Benefited:
        return BenefitedRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteBenefitedCommand) -> bool:
        return BenefitedRepository.delete(command.id)
