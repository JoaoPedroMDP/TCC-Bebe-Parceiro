#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.app_views import BaseView
from core.cqrs.commands.speciality_commands import (CreateSpecialityCommand, PatchSpecialityCommand,
                                                    DeleteSpecialityCommand)
from core.cqrs.queries.speciality_queries import GetSpecialityQuery, ListSpecialityQuery
from core.models import Speciality
from core.serializers import SpecialitySerializer
from core.services.speciality_service import SpecialityService
from core.utils.decorators import endpoint
from config import MANAGE_SPECIALITIES
from core.permissions.at_least_one_group import AtLeastOneGroup
from core.permissions.owns_it import OwnsIt

lgr = logging.getLogger(__name__)


class SpecialityGenericViews(BaseView):
    groups = [MANAGE_SPECIALITIES]
    permission_classes = (AtLeastOneGroup,)
    authentication_classes_by_method = {
        "get": (),
    }
    permission_classes_by_method = {
        "get": (),
    }

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_SPECIALITIES----")
        list_specialities_query: ListSpecialityQuery = ListSpecialityQuery.from_dict(request.query_params)
        specialities: List[Speciality] = SpecialityService.filter(list_specialities_query)
        return SpecialitySerializer(specialities, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_SPECIALITY----")
        command: CreateSpecialityCommand = CreateSpecialityCommand.from_dict(request.data)
        new_speciality: Speciality = SpecialityService.create(command)

        return SpecialitySerializer(new_speciality).data, status.HTTP_201_CREATED


class SpecialitySpecificViews(BaseView):
    groups = [MANAGE_SPECIALITIES]
    permission_classes = (AtLeastOneGroup,)
    permission_classes_by_method = {
    }
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_SPECIALITY----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchSpecialityCommand = PatchSpecialityCommand.from_dict(data)
        patched_speciality: Speciality = SpecialityService.patch(command)

        return SpecialitySerializer(patched_speciality).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_SPECIALITY----")
        command: DeleteSpecialityCommand = DeleteSpecialityCommand.from_dict({'id': int(pk)})
        deleted: bool = SpecialityService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_SPECIALITY----")
        query: GetSpecialityQuery = GetSpecialityQuery.from_dict({"id": pk})
        speciality: Speciality = SpecialityService.get(query)

        if speciality:
            return SpecialitySerializer(speciality).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
