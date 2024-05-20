#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request

from config import MANAGE_ACCESS_CODES
from core.app_views import BaseView
from core.cqrs.commands.access_code_commands import CreateAccessCodeCommand, PatchAccessCodeCommand, \
    DeleteAccessCodeCommand
from core.cqrs.queries.access_code_queries import GetAccessCodeQuery, ListAccessCodeQuery, CheckAccessCodeQuery
from core.models import AccessCode
from core.permissions.at_least_one_group import AtLeastOneGroup
from core.serializers import AccessCodeSerializer
from core.services.access_code_service import AccessCodeService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class AccessCodeGenericViews(BaseView):
    groups = [MANAGE_ACCESS_CODES]
    permission_classes = (AtLeastOneGroup,)

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_ACCESS-CODES----")
        list_access_codes_query: ListAccessCodeQuery = ListAccessCodeQuery.from_dict(request.query_params)
        access_codes: List[AccessCode] = AccessCodeService.filter(list_access_codes_query)
        return AccessCodeSerializer(access_codes, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_ACCESS-CODE----")
        command: CreateAccessCodeCommand = CreateAccessCodeCommand.from_dict(request.data)
        command.user = request.user
        new_access_codes: List[AccessCode] = AccessCodeService.create(command)

        return AccessCodeSerializer(new_access_codes, many=True).data, status.HTTP_201_CREATED


class AccessCodeSpecificViews(BaseView):
    groups = [MANAGE_ACCESS_CODES]
    permission_classes = (AtLeastOneGroup,)

    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_ACCESS-CODE----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchAccessCodeCommand = PatchAccessCodeCommand.from_dict(data)
        patched_access_code: AccessCode = AccessCodeService.patch(command)

        return AccessCodeSerializer(patched_access_code).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_ACCESS-CODE----")
        command: DeleteAccessCodeCommand = DeleteAccessCodeCommand.from_dict({'id': int(pk)})
        deleted: bool = AccessCodeService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_ACCESS-CODE----")
        query: GetAccessCodeQuery = GetAccessCodeQuery.from_dict({"id": pk})
        access_code: AccessCode = AccessCodeService.get(query)
        if access_code:
            return AccessCodeSerializer(access_code).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND


class CheckAccessCodeView(BaseView):
    authentication_classes = []
    permission_classes = (AllowAny,)

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----CHECK_ACCESS-CODE----")
        query: CheckAccessCodeQuery = CheckAccessCodeQuery.from_dict(request.query_params)
        access_code: AccessCode = AccessCodeService.get_by_code(query.code)
        if access_code:
            if access_code.used is False:
                return {"messsage": "Código válido."}, status.HTTP_200_OK
            else:
                return {"messsage": "Código inválido."}, status.HTTP_403_FORBIDDEN

        return {"messsage": "Código não encontrado."}, status.HTTP_404_NOT_FOUND
