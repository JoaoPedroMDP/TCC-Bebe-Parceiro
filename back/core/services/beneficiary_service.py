#  coding: utf-8
import logging
from typing import List

from rest_framework import status

from core.cqrs.commands.appointment_commands import CreateAppointmentCommand
from core.cqrs.commands.beneficiary_commands import CreateBeneficiaryCommand, PatchBeneficiaryCommand, \
    DeleteBeneficiaryCommand, ApproveBeneficiaryCommand
from core.cqrs.commands.child_commands import CreateChildCommand, PatchChildCommand
from core.cqrs.commands.user_commands import CreateUserCommand, PatchUserCommand
from core.cqrs.queries.beneficiary_queries import GetBeneficiaryQuery, ListBeneficiaryQuery
from core.models import Beneficiary
from core.repositories.access_code_repository import AccessCodeRepository
from core.repositories.beneficiary_repository import BeneficiaryRepository
from core.repositories.city_repository import CityRepository
from core.repositories.marital_status_repository import MaritalStatusRepository
from core.repositories.social_program_repository import SocialProgramRepository
from core.services import CrudService
from core.services.appointment_service import AppointmentService
from core.services.child_service import ChildService
from core.services.user_service import UserService
from core.utils.exceptions import HttpFriendlyError


lgr = logging.getLogger(__name__)


class BeneficiaryService(CrudService):
    @classmethod
    def create(cls, command: CreateBeneficiaryCommand) -> Beneficiary:
        # Verifica se o estado civil passado é válido
        marital_status = MaritalStatusRepository.get(command.marital_status_id)

        # Verifica se a cidade passada é válida
        city = CityRepository.get(command.city_id)

        access_codes = []
        if command.access_code:
            # Verifico se o código de acesso já existe e não foi usado
            access_codes = AccessCodeRepository.filter(code=command.access_code, used=False)
            if not access_codes:
                raise HttpFriendlyError("Código de acesso inválido", status.HTTP_400_BAD_REQUEST)

        # Verifico se os programas sociais existem de fato
        social_programs = []
        if command.social_programs:
            for social_program in command.social_programs:
                social_programs.append(SocialProgramRepository.get(social_program['id']))

        new_user = UserService.create(CreateUserCommand.from_dict(command.to_dict()))

        data = command.to_dict()
        data['approved'] = False

        # Relacionamentos N:N eu associo depois
        del data["children"]
        if "social_programs" in data:
            del data["social_programs"]

        try:
            new_beneficiary = Beneficiary()
            new_beneficiary = BeneficiaryRepository.fill(data, new_beneficiary)
            new_beneficiary.user = new_user
            new_beneficiary.city = city

            new_beneficiary.save()
        except Exception as e:
            new_user.delete()
            raise e

        # Vinculo a beneficiada aos programas sociais
        new_beneficiary.marital_status = marital_status
        for social_program in social_programs:
            new_beneficiary.social_programs.add(social_program)

        if command.access_code:
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
        beneficiary: Beneficiary = BeneficiaryRepository.get(command.id)

        if command.user_data:
            user_command = PatchUserCommand.from_dict({
                **command.user_data,
                'id': beneficiary.user.id
            })
            UserService.patch(user_command)

        if command.children:
            for child in command.children:
                c_command = PatchChildCommand.from_dict(child)
                ChildService.patch(c_command)
            
            command.children = None

        if command.social_programs:
            beneficiary.social_programs.clear()
            for social_p in command.social_programs:
                beneficiary.social_programs.add(SocialProgramRepository.get(social_p['id']))
            
            command.social_programs = None


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

    @classmethod
    def anonimize(cls, command: DeleteBeneficiaryCommand) -> Beneficiary:
        beneficiary: Beneficiary = BeneficiaryRepository.get(command.id)
        beneficiary.user.first_name = 'ANONIMIZADO'
        beneficiary.user.last_name = 'ANONIMIZADO'
        beneficiary.user.email = 'ANONIMIZADO'
        beneficiary.user.phone = 'ANONIMIZADO'
        beneficiary.user.save()

        for child in beneficiary.children.all():
            child.name = 'ANONIMIZADO'
            child.save()

        return beneficiary #ver se retorna so um true ou se n retorna nada ou desse jeito (retornando obj atualizado)
    
    @classmethod
    def approve_beneficiary(cls, command: ApproveBeneficiaryCommand) -> Beneficiary:
        beneficiary: Beneficiary = BeneficiaryRepository.get(command.id)
        ca_command: CreateAppointmentCommand = CreateAppointmentCommand.from_dict(command.appointment_data)
        ca_command.user = command.user

        beneficiary.approved = True
        beneficiary.save()
        
        AppointmentService.create(ca_command)

        return beneficiary

    @classmethod
    def get_pending_beneficiaries(cls):
        return BeneficiaryRepository.filter(approved=False)

    @classmethod
    def can_request_swap(cls, beneficiary: Beneficiary) -> bool:
        return not beneficiary.has_pending_swap() and beneficiary.have_children_born()
