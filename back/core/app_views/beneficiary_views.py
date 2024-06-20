#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request

from config import MANAGE_BENEFICIARIES, MANAGE_REGISTRATIONS, MANAGE_REPORTS
from core.app_views import BaseView
from core.cqrs.commands.beneficiary_commands import CreateBeneficiaryCommand, PatchBeneficiaryCommand, \
    DeleteBeneficiaryCommand, ApproveBeneficiaryCommand
from core.cqrs.commands.user_commands import DeleteUserCommand
from core.cqrs.queries.beneficiary_queries import GetBeneficiariesReportQuery, GetBeneficiaryQuery, ListBeneficiaryQuery
from core.models import Beneficiary
from core.permissions.at_least_one_group import AtLeastOneGroup
from core.permissions.is_volunteer import IsVolunteer
from core.permissions.volunteer_at_least_one_group import VolunteerAtLeastOneGroup
from core.permissions.is_beneficiary import IsBeneficiary
from core.permissions.is_it import IsIt
from core.repositories.beneficiary_repository import BeneficiaryRepository
from core.serializers import BeneficiarySerializer
from core.services.beneficiary_service import BeneficiaryService
from core.services.user_service import UserService
from core.utils.decorators import endpoint
from rest_framework.permissions import IsAuthenticated

lgr = logging.getLogger(__name__)


class BeneficiaryCreationByVolunteerView(BaseView):
    groups = [MANAGE_BENEFICIARIES]
    permission_classes = (IsAuthenticated, IsVolunteer, VolunteerAtLeastOneGroup,)

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_BENEFICIARY_BY_VOLUNTEER----")
        command: CreateBeneficiaryCommand = CreateBeneficiaryCommand.from_dict({
            **request.data,
            'user': request.user
        })

        new_beneficiary: Beneficiary = BeneficiaryService.create(command)

        return BeneficiarySerializer(new_beneficiary).data, status.HTTP_201_CREATED


class BeneficiaryGenericViews(BaseView):
    groups = [MANAGE_BENEFICIARIES, MANAGE_REPORTS]
    permission_classes = (IsAuthenticated, VolunteerAtLeastOneGroup, IsVolunteer)
    permission_classes_by_method = {
        "post": ()
    }
    authentication_classes_by_method = {
        "post": ()
    }

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_BENEFICIARIES----")
        data = copy(request.query_params)
        data['approved'] = True
        list_beneficiaries_query: ListBeneficiaryQuery = ListBeneficiaryQuery.from_dict(data)
        beneficiaries: List[Beneficiary] = BeneficiaryService.filter(list_beneficiaries_query)
        
        return BeneficiarySerializer(beneficiaries, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_BENEFICIARY----")
        command: CreateBeneficiaryCommand = CreateBeneficiaryCommand.from_dict(request.data)
        new_beneficiary: Beneficiary = BeneficiaryService.create(command)

        return BeneficiarySerializer(new_beneficiary).data, status.HTTP_201_CREATED


class BeneficiarySpecificViews(BaseView):
    groups = [MANAGE_BENEFICIARIES]
    permission_classes = [IsAuthenticated, ((IsVolunteer & VolunteerAtLeastOneGroup) | IsIt)]

    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_BENEFICIARY----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchBeneficiaryCommand = PatchBeneficiaryCommand.from_dict(data)
        patched_beneficiary: Beneficiary = BeneficiaryService.patch(command)

        return BeneficiarySerializer(patched_beneficiary).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_BENEFICIARY----")
        beneficiary: Beneficiary = BeneficiaryRepository.get(pk)
        command_user: DeleteUserCommand = DeleteUserCommand.from_dict({'id': beneficiary.user_id})
        command: DeleteBeneficiaryCommand = DeleteBeneficiaryCommand.from_dict({'id': int(pk)})

        if request.user.is_beneficiary():
            anonimized: Beneficiary = BeneficiaryService.anonimize(command)
            return {"message": "Beneficiária anonimizada."}, status.HTTP_204_NO_CONTENT
        else:
            # Aqui chamamos o delete de User para apagar tudo (user, beneficiary e child, visto que são filhos de user)
            deleted: bool = UserService.delete(command_user)
            return {"message": "Beneficiária deletada."}, status.HTTP_204_NO_CONTENT

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_BENEFICIARY----")
        query: GetBeneficiaryQuery = GetBeneficiaryQuery.from_dict({"id": pk})
        beneficiary: Beneficiary = BeneficiaryService.get(query)
        if beneficiary:
            return BeneficiarySerializer(beneficiary).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND

class BeneficiaryApprovalView(BaseView):
    groups = [MANAGE_REGISTRATIONS]
    permission_classes = (IsAuthenticated, IsVolunteer, VolunteerAtLeastOneGroup)

    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----APPROVE_BENEFICIARY----")
        data = copy(request.data)
        data['beneficiary_id'] = pk
        data['user'] = request.user
        command: ApproveBeneficiaryCommand = ApproveBeneficiaryCommand.from_dict(data)
        command.user = request.user
        approved_beneficiary: Beneficiary = BeneficiaryService.approve_beneficiary(command)

        return BeneficiarySerializer(approved_beneficiary).data, status.HTTP_200_OK


class BeneficiaryPendingView(BaseView):
    groups = [MANAGE_REGISTRATIONS]
    permission_classes = (IsAuthenticated, IsVolunteer, AtLeastOneGroup)

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_PENDING_BENEFICIARIES----")
        beneficiaries: List[Beneficiary] = BeneficiaryService.get_pending_beneficiaries()
        return BeneficiarySerializer(beneficiaries, many=True).data, status.HTTP_200_OK


class BeneficiaryCanRequestSwapView(BaseView):
    permission_classes = [IsAuthenticated, IsBeneficiary]

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----CAN_REQUEST_SWAP----")
        beneficiary: Beneficiary = request.user.beneficiary
        return {
            'can_request_swap': BeneficiaryService.can_request_swap(beneficiary)
        }, status.HTTP_200_OK


class BeneficiaryReportsView(BaseView):
    groups = [MANAGE_REPORTS]
    permission_classes = [IsAuthenticated, IsVolunteer, AtLeastOneGroup]

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_BENEFICIARIES_REPORTS----")
        query: GetBeneficiariesReportQuery = GetBeneficiariesReportQuery.from_dict(request.query_params)
        beneficiaries: List[Beneficiary] = BeneficiaryService.get_reports(query)
        return BeneficiarySerializer(beneficiaries, many=True).data, status.HTTP_200_OK
