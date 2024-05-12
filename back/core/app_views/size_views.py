#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request

from config import MANAGE_SIZES
from core.app_views import BaseView
from core.cqrs.commands.size_commands import CreateSizeCommand, PatchSizeCommand, \
    DeleteSizeCommand
from core.cqrs.queries.size_queries import GetSizeQuery, ListSizeQuery
from core.models import Size
from core.permissions.is_volunteer import IsVolunteer
from core.permissions.volunteer_at_least_one_group import VolunteerAtLeastOneGroup
from core.serializers import SizeSerializer
from core.services.size_service import SizeService
from core.utils.decorators import endpoint
from rest_framework.permissions import IsAuthenticated

lgr = logging.getLogger(__name__)


class SizeGenericViews(BaseView):
    groups = [MANAGE_SIZES]
    permission_classes = [IsAuthenticated]
    permission_classes_by_method = {
        "post": [IsVolunteer & VolunteerAtLeastOneGroup]
    }
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_SIZES----")
        list_sizes_query: ListSizeQuery = ListSizeQuery.from_dict(request.query_params)
        sizes: List[Size] = SizeService.filter(list_sizes_query)
        return SizeSerializer(sizes, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_SIZE----")
        command: CreateSizeCommand = CreateSizeCommand.from_dict(request.data)
        new_size: Size = SizeService.create(command)

        return SizeSerializer(new_size).data, status.HTTP_201_CREATED


class SizeSpecificViews(BaseView):
    groups = [MANAGE_SIZES]
    permission_classes = [IsVolunteer & VolunteerAtLeastOneGroup]
    permission_classes_by_method = {
        "get": [IsAuthenticated]
    }

    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_SIZE----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchSizeCommand = PatchSizeCommand.from_dict(data)
        patched_size: Size = SizeService.patch(command)

        return SizeSerializer(patched_size).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_SIZE----")
        command: DeleteSizeCommand = DeleteSizeCommand.from_dict({'id': int(pk)})
        deleted: bool = SizeService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_SIZE----")
        query: GetSizeQuery = GetSizeQuery.from_dict({"id": pk})
        size: Size = SizeService.get(query)

        if size:
            return SizeSerializer(size).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
