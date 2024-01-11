#  coding: utf-8
from typing import List

from rest_framework import status

from core.cqrs.commands.beneficiary_commands import CreateBeneficiaryCommand, PatchBeneficiaryCommand, \
    DeleteBeneficiaryCommand
from core.cqrs.commands.child_commands import CreateChildCommand
from core.cqrs.commands.user_commands import CreateUserCommand
from core.cqrs.queries.beneficiary_queries import GetBeneficiaryQuery, ListBeneficiaryQuery
from core.models import Beneficiary
from core.repositories.access_code_repository import AccessCodeRepository
from core.repositories.beneficiary_repository import BeneficiaryRepository
from core.repositories.city_repository import CityRepository
from core.repositories.marital_status_repository import MaritalStatusRepository
from core.repositories.social_program_repository import SocialProgramRepository
from core.services import CrudService
from core.services.child_service import ChildService
from core.services.user_service import UserService
from core.utils.exceptions import HttpFriendlyError


class BeneficiaryService(CrudService):
    @classmethod
    def create(cls, command: CreateBeneficiaryCommand) -> Beneficiary:
        # Verifica se o estado civil passado é válido
        marital_status = MaritalStatusRepository.get(command.marital_status_id)

        # Verifica se a cidade passada é válida
        city = CityRepository.get(command.city_id)

        # Verifico se o código de acesso já existe e não foi usado
        access_codes = AccessCodeRepository.filter(code=command.access_code, used=False)
        if not access_codes:
            raise HttpFriendlyError("Código de acesso inválido", status.HTTP_400_BAD_REQUEST)

        # Verifico se os programas sociais existem de fato
        social_programs = []
        if command.social_programs:
            for social_program_id in command.social_programs:
                social_programs.append(SocialProgramRepository.get(social_program_id))

        new_user = UserService.create(CreateUserCommand.from_dict(command.to_dict()))

        data = command.to_dict()
        # As crianças eu associo depois
        del data["children"]

        # Vinculo a beneficiada aos programas sociais
        try:
            new_beneficiary = Beneficiary()
            new_beneficiary = BeneficiaryRepository.fill(data, new_beneficiary)
            new_beneficiary.user = new_user
            new_beneficiary.city = city
            new_beneficiary.marital_status = marital_status

            for social_program in social_programs:
                new_beneficiary.social_programs.add(social_program)

            new_beneficiary.save()
        except Exception as e:
            new_user.delete()
            raise e

        # Pego o primeiro código de acesso válido (deveria haver apenas um, vem em lista porque é 'filter')
        access_code = access_codes[0]
        access_code.used = True
        AccessCodeRepository.patch(access_code.to_dict())

        # Armazeno os filhos da beneficiada
        for child in command.children:
            child["beneficiary_id"] = new_beneficiary.id
            command = CreateChildCommand.from_dict(child)
            ChildService.create(command)

        return new_beneficiary

    @classmethod
    def patch(cls, command: PatchBeneficiaryCommand) -> Beneficiary:
        return BeneficiaryRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListBeneficiaryQuery) -> List[Beneficiary]:
        return BeneficiaryRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetBeneficiaryQuery) -> Beneficiary:
        return BeneficiaryRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteBeneficiaryCommand) -> bool:
        return BeneficiaryRepository.delete(command.id)
