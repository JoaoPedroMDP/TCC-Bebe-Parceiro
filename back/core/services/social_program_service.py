#  coding: utf-8
from typing import List

from core.cqrs.commands.social_program_commands import CreateSocialProgramCommand, PatchSocialProgramCommand, \
    DeleteSocialProgramCommand
from core.cqrs.queries.social_program_queries import GetSocialProgramQuery, ListSocialProgramQuery
from core.models import SocialProgram
from core.repositories.social_program_repository import SocialProgramRepository
from core.services import Service


class SocialProgramService(Service):
    @classmethod
    def create(cls, command: CreateSocialProgramCommand) -> SocialProgram:
        new_program = SocialProgramRepository.create(command.to_dict())
        return new_program

    @classmethod
    def patch(cls, command: PatchSocialProgramCommand) -> SocialProgram:
        return SocialProgramRepository.patch(command.to_dict())

    @classmethod
    def list(cls, query: ListSocialProgramQuery) -> List[SocialProgram]:
        return SocialProgramRepository.list(**query.to_dict())

    @classmethod
    def get(cls, query: GetSocialProgramQuery) -> SocialProgram:
        return SocialProgramRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteSocialProgramCommand) -> bool:
        return SocialProgramRepository.delete(command.id)
