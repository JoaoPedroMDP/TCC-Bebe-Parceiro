#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.marital_status_commands import CreateMaritalStatusCommand, PatchMaritalStatusCommand, \
    DeleteMaritalStatusCommand
from core.cqrs.queries.marital_status_queries import GetMaritalStatusQuery, ListMaritalStatusQuery
from core.models import MaritalStatus
from core.serializers import MaritalStatusSerializer
from core.services.marital_status_service import MaritalStatusService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class MaritalStatusGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_MARITAL-STATUSS----")
        list_marital_statuss_query: ListMaritalStatusQuery = ListMaritalStatusQuery.from_dict(request.query_params)
        marital_statuss: List[MaritalStatus] = MaritalStatusService.filter(list_marital_statuss_query)
        return MaritalStatusSerializer(marital_statuss, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_MARITAL-STATUS----")
        command: CreateMaritalStatusCommand = CreateMaritalStatusCommand.from_dict(request.data)
        new_marital_status: MaritalStatus = MaritalStatusService.create(command)

        return MaritalStatusSerializer(new_marital_status).data, status.HTTP_201_CREATED


class MaritalStatusSpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_MARITAL-STATUS----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchMaritalStatusCommand = PatchMaritalStatusCommand.from_dict(data)
        patched_marital_status: MaritalStatus = MaritalStatusService.patch(command)

        return MaritalStatusSerializer(patched_marital_status).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_MARITAL-STATUS----")
        command: DeleteMaritalStatusCommand = DeleteMaritalStatusCommand.from_dict({'id': int(pk)})
        deleted: bool = MaritalStatusService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_MARITAL-STATUS----")
        query: GetMaritalStatusQuery = GetMaritalStatusQuery.from_dict({"id": pk})
        marital_status: MaritalStatus = MaritalStatusService.get(query)
        if marital_status:
            return MaritalStatusSerializer(marital_status).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
