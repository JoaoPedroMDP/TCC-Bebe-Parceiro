#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.child_commands import CreateChildCommand, PatchChildCommand, \
    DeleteChildCommand
from core.cqrs.queries.child_queries import GetChildQuery, ListChildQuery
from core.models import Child
from core.serializers import ChildSerializer
from core.services.child_service import ChildService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class ChildGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_CHILDREN----")
        list_cities_query: ListChildQuery = ListChildQuery.from_dict(request.query_params)
        cities: List[Child] = ChildService.filter(list_cities_query)
        return ChildSerializer(cities, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_CHILD----")
        command: CreateChildCommand = CreateChildCommand.from_dict(request.data)
        new_child: Child = ChildService.create(command)

        return ChildSerializer(new_child).data, status.HTTP_201_CREATED


class ChildSpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_CHILD----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchChildCommand = PatchChildCommand.from_dict(data)
        patched_child: Child = ChildService.patch(command)

        return ChildSerializer(patched_child).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_CHILD----")
        command: DeleteChildCommand = DeleteChildCommand.from_dict({'id': int(pk)})
        deleted: bool = ChildService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_CHILD----")
        query: GetChildQuery = GetChildQuery.from_dict({"id": pk})
        child: Child = ChildService.get(query)
        if Child:
            return ChildSerializer(child).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
