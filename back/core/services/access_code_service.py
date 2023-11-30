#  coding: utf-8
import logging
import random
import string
from typing import List

from core.cqrs.commands.access_code_commands import CreateAccessCodeCommand, PatchAccessCodeCommand, \
    DeleteAccessCodeCommand
from core.cqrs.queries.access_code_queries import GetAccessCodeQuery, ListAccessCodeQuery
from core.models import AccessCode
from core.repositories.access_code_repository import AccessCodeRepository
from core.services import Service

lgr = logging.getLogger(__name__)


class AccessCodeService(Service):

    @classmethod
    def generate_code(cls, prefix: str):
        letters = string.ascii_uppercase
        first_triad = ''.join(random.choice(string.digits) for i in range(3))
        second_triad = ''.join(random.choice(letters) for i in range(3))
        return prefix.upper() + first_triad + second_triad

    @classmethod
    def create(cls, command: CreateAccessCodeCommand) -> AccessCode:
        # O código deve ser no formato prefix + 3 números + 3 letras, tudo maiúsculo
        code = cls.generate_code(command.prefix)
        while AccessCode.objects.filter(code=code).exists():
            lgr.warning("Código {} já existe, gerando outro".format(code))
            code = cls.generate_code(command.prefix)

        return AccessCodeRepository.create({"code": code})

    @classmethod
    def patch(cls, command: PatchAccessCodeCommand) -> AccessCode:
        return AccessCodeRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListAccessCodeQuery) -> List[AccessCode]:
        lgr.debug("Listando com filtros: {}".format(query.to_dict()))
        return AccessCodeRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetAccessCodeQuery) -> AccessCode:
        return AccessCodeRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteAccessCodeCommand) -> bool:
        return AccessCodeRepository.delete(command.id)
