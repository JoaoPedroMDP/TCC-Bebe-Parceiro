#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request

from config import MANAGE_REPORTS, MANAGE_SWAPS
from core.app_views import BaseView
from core.cqrs.commands.swap_commands import CreateSwapCommand, PatchSwapCommand, \
    DeleteSwapCommand
from core.cqrs.queries.swap_queries import GetSwapQuery, GetSwapsReportQuery, ListSwapQuery
from core.models import Swap
from core.permissions.at_least_one_group import AtLeastOneGroup
from core.permissions.beneficiary_owns_swap import BeneficiaryOwnsSwap
from core.permissions.is_volunteer import IsVolunteer
from core.permissions.volunteer_at_least_one_group import VolunteerAtLeastOneGroup
from core.serializers import SwapSerializer
from core.services.swap_service import SwapService
from core.utils.decorators import endpoint
from rest_framework.permissions import IsAuthenticated

lgr = logging.getLogger(__name__)


class SwapGenericViews(BaseView):
    groups = [MANAGE_SWAPS, MANAGE_REPORTS]
    permission_classes = [IsAuthenticated, VolunteerAtLeastOneGroup]

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_SWAPS----")
        list_swaps_query: ListSwapQuery = ListSwapQuery.from_dict(request.query_params)
        list_swaps_query.user = request.user
        
        swaps: List[Swap] = SwapService.filter(list_swaps_query)
        return SwapSerializer(swaps, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_SWAP----")
        data = copy(request.data)
        data['user'] = request.user
        command: CreateSwapCommand = CreateSwapCommand.from_dict(data)
        new_swap: Swap = SwapService.create(command)

        return SwapSerializer(new_swap).data, status.HTTP_201_CREATED


class SwapSpecificViews(BaseView):
    groups = [MANAGE_SWAPS]
    permission_classes = [IsVolunteer & VolunteerAtLeastOneGroup]
    permission_classes_by_method = {
        "get": [VolunteerAtLeastOneGroup & BeneficiaryOwnsSwap]
    }

    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_SWAP----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchSwapCommand = PatchSwapCommand.from_dict(data)
        patched_swap: Swap = SwapService.patch(command)

        return SwapSerializer(patched_swap).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_SWAP----")
        command: DeleteSwapCommand = DeleteSwapCommand.from_dict({'id': int(pk)})
        deleted: bool = SwapService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_SWAP----")
        query: GetSwapQuery = GetSwapQuery.from_dict({"id": pk})
        swap: Swap = SwapService.get(query)

        if swap:
            return SwapSerializer(swap).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND


class SwapReportsView(BaseView):
    groups = [MANAGE_REPORTS]
    permission_classes = [IsAuthenticated, IsVolunteer, AtLeastOneGroup]

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_SWAPS_REPORTS----")
        query: GetSwapsReportQuery = GetSwapsReportQuery.from_dict(request.query_params)
        swaps: List[Swap] = SwapService.get_reports(query)
        return SwapSerializer(swaps, many=True).data, status.HTTP_200_OK
