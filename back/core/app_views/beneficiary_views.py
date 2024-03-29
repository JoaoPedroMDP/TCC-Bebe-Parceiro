#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.beneficiary_commands import CreateBeneficiaryCommand, PatchBeneficiaryCommand, \
    DeleteBeneficiaryCommand
from core.cqrs.queries.beneficiary_queries import GetBeneficiaryQuery, ListBeneficiaryQuery
from core.models import Beneficiary
from core.serializers import BeneficiarySerializer
from core.services.beneficiary_service import BeneficiaryService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class BeneficiaryGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_BENEFICIARIES----")
        list_beneficiaries_query: ListBeneficiaryQuery = ListBeneficiaryQuery.from_dict(request.query_params)
        beneficiaries: List[Beneficiary] = BeneficiaryService.filter(list_beneficiaries_query)
        return BeneficiarySerializer(beneficiaries, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_BENEFITED----")
        command: CreateBeneficiaryCommand = CreateBeneficiaryCommand.from_dict(request.data)
        new_beneficiary: Beneficiary = BeneficiaryService.create(command)

        return BeneficiarySerializer(new_beneficiary).data, status.HTTP_201_CREATED


class BeneficiarySpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_BENEFITED----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchBeneficiaryCommand = PatchBeneficiaryCommand.from_dict(data)
        patched_beneficiary: Beneficiary = BeneficiaryService.patch(command)

        return BeneficiarySerializer(patched_beneficiary).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_BENEFITED----")
        command: DeleteBeneficiaryCommand = DeleteBeneficiaryCommand.from_dict({'id': int(pk)})
        deleted: bool = BeneficiaryService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_BENEFITED----")
        query: GetBeneficiaryQuery = GetBeneficiaryQuery.from_dict({"id": pk})
        beneficiary: Beneficiary = BeneficiaryService.get(query)
        if beneficiary:
            return BeneficiarySerializer(beneficiary).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
