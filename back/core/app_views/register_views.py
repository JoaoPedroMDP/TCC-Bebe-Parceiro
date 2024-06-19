#  coding: utf-8

from copy import copy
import logging
from typing import List
from config import MANAGE_EVALUATIONS
from core.app_views import BaseView
from core.cqrs.commands.register_commands import CreateRegisterCommand, DeleteRegisterCommand, PatchRegisterCommand
from core.cqrs.queries.register_queries import GetRegisterQuery, ListRegisterQuery
from core.models import Register
from core.permissions.at_least_one_group import AtLeastOneGroup
from core.permissions.is_volunteer import IsVolunteer
from core.serializers import RegisterSerializer
from core.services.register_service import RegisterService
from core.utils.decorators import endpoint
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


lgr = logging.getLogger(__name__)


class RegisterGenericView(BaseView):
    groups = [MANAGE_EVALUATIONS]
    permission_classes = (IsAuthenticated, IsVolunteer, AtLeastOneGroup,)

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_REGISTERS----")
        list_registers_query: ListRegisterQuery = ListRegisterQuery.from_dict(request.query_params)
        registers: List[Register] = RegisterService.filter(list_registers_query)
        return RegisterSerializer(registers, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_REGISTER----")
        command: CreateRegisterCommand = CreateRegisterCommand.from_dict(request.data)
        new_register: Register = RegisterService.create(command)

        return RegisterSerializer(new_register).data, status.HTTP_201_CREATED


class RegisterSpecificView(BaseView):
    groups = [MANAGE_EVALUATIONS]
    permission_classes = (IsAuthenticated, IsVolunteer, AtLeastOneGroup,)
    
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_REGISTER----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchRegisterCommand = PatchRegisterCommand.from_dict(data)
        patched_register: Register = RegisterService.patch(command)

        return RegisterSerializer(patched_register).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_REGISTER----")
        command: DeleteRegisterCommand = DeleteRegisterCommand.from_dict({'id': int(pk)})
        deleted: bool = RegisterService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_REGISTER----")
        query: GetRegisterQuery = GetRegisterQuery.from_dict({"id": pk})
        register: Register = RegisterService.get(query)

        if register:
            return RegisterSerializer(register).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
