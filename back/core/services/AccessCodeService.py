#  coding: utf-8
import random
import string
from typing import List

from core.cqrs.commands.access_code_commands import CreateAccessCodeCommand
from core.models import AccessCode


class AccessCodeService:
    @staticmethod
    def create(command: CreateAccessCodeCommand) -> AccessCode:
        # O código deve ser no formato prefix + 6 caracteres aleatórios
        letters = string.ascii_uppercase
        code = command.prefix.upper() + "-" + ''.join(random.choice(letters) for i in range(6))
        new_code = AccessCode(code=code)
        new_code.save()
        return new_code

    def patch(self):
        pass

    @staticmethod
    def list() -> List[AccessCode]:
        return AccessCode.objects.all()

    def get(self):
        pass

    def delete(self):
        pass
