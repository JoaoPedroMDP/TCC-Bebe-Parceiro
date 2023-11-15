#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.benefited_commands import CreateBenefitedCommand, PatchBenefitedCommand, \
    DeleteBenefitedCommand
from core.cqrs.queries.benefited_queries import GetBenefitedQuery, ListBenefitedQuery
from core.models import Benefited
from core.serializers import BenefitedSerializer
from core.services.benefited_service import BenefitedService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class BenefitedGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_BENEFICIARIES----")
        list_beneficiaries_query: ListBenefitedQuery = ListBenefitedQuery.from_dict(request.query_params)
        beneficiaries: List[Benefited] = BenefitedService.list(list_beneficiaries_query)
        return BenefitedSerializer(beneficiaries, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_BENEFITED----")
        command: CreateBenefitedCommand = CreateBenefitedCommand.from_dict(request.data)
        new_benefited: Benefited = BenefitedService.create(command)

        return BenefitedSerializer(new_benefited).data, status.HTTP_201_CREATED


class BenefitedSpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_BENEFITED----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchBenefitedCommand = PatchBenefitedCommand.from_dict(data)
        patched_benefited: Benefited = BenefitedService.patch(command)

        return BenefitedSerializer(patched_benefited).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_BENEFITED----")
        command: DeleteBenefitedCommand = DeleteBenefitedCommand.from_dict({'id': int(pk)})
        deleted: bool = BenefitedService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_BENEFITED----")
        query: GetBenefitedQuery = GetBenefitedQuery.from_dict({"id": pk})
        benefited: Benefited = BenefitedService.get(query)
        if benefited:
            return BenefitedSerializer(benefited).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
