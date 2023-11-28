#  coding: utf-8
from typing import List

from rest_framework import status

from core.cqrs.commands.benefited_commands import CreateBenefitedCommand, PatchBenefitedCommand, \
    DeleteBenefitedCommand
from core.cqrs.commands.child_commands import CreateChildCommand
from core.cqrs.queries.benefited_queries import GetBenefitedQuery, ListBenefitedQuery
from core.models import Beneficiary
from core.repositories.access_code_repository import AccessCodeRepository
from core.repositories.benefited_repository import BenefitedRepository
from core.repositories.city_repository import CityRepository
from core.repositories.marital_status_repository import MaritalStatusRepository
from core.repositories.social_program_repository import SocialProgramRepository
from core.services import Service
from core.services.child_service import ChildService
from core.utils.exceptions import HttpFriendlyError


class BenefitedService(Service):
    @classmethod
    def create(cls, command: CreateBenefitedCommand) -> Beneficiary:
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

        data = {
            "name": command.name,
            "email": command.email,
            "phone": command.phone,
            "password": command.password,
            "birth_date": command.birth_date,
            "child_count": command.child_count,
            "monthly_familiar_income": command.monthly_familiar_income,
            "has_disablement": command.has_disablement,
            "city": city,
            "marital_status": marital_status,
        }

        # Vinculo a beneficiada aos programas sociais
        new_benefited = BenefitedRepository.create(data)
        for social_program in social_programs:
            new_benefited.social_programs.add(social_program)

        new_benefited.save()

        # Pego o primeiro código de acesso válido (deveria haver apenas um, vem em lista porque é 'filter')
        access_code = access_codes[0]
        access_code.used = True
        AccessCodeRepository.patch(access_code.to_dict())

        # Armazeno os filhos da beneficiada
        for child in command.children:
            child["benefited_id"] = new_benefited.id
            command = CreateChildCommand.from_dict(child)
            ChildService.create(command)

        return new_benefited

    @classmethod
    def patch(cls, command: PatchBenefitedCommand) -> Beneficiary:
        return BenefitedRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListBenefitedQuery) -> List[Beneficiary]:
        return BenefitedRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetBenefitedQuery) -> Beneficiary:
        return BenefitedRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteBenefitedCommand) -> bool:
        return BenefitedRepository.delete(command.id)
