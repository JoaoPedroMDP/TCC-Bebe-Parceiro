#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.volunteer_commands import CreateVolunteerCommand, PatchVolunteerCommand, \
    DeleteVolunteerCommand
from core.cqrs.queries.volunteer_queries import GetVolunteerQuery, ListVolunteerQuery
from core.models import Volunteer
from core.serializers import VolunteerSerializer
from core.services.volunteer_service import VolunteerService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class VolunteerGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_VOLUNTEERS----")
        list_volunteers_query: ListVolunteerQuery = ListVolunteerQuery.from_dict(request.query_params)
        volunteers: List[Volunteer] = VolunteerService.filter(list_volunteers_query)
        return VolunteerSerializer(volunteers, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_VOLUNTEER----")
        command: CreateVolunteerCommand = CreateVolunteerCommand.from_dict(request.data)
        new_volunteer: Volunteer = VolunteerService.create(command)

        return VolunteerSerializer(new_volunteer).data, status.HTTP_201_CREATED


class VolunteerSpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_VOLUNTEER----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchVolunteerCommand = PatchVolunteerCommand.from_dict(data)
        patched_volunteer: Volunteer = VolunteerService.patch(command)

        return VolunteerSerializer(patched_volunteer).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_VOLUNTEER----")
        command: DeleteVolunteerCommand = DeleteVolunteerCommand.from_dict({'id': int(pk)})
        deleted: bool = VolunteerService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_VOLUNTEER----")
        query: GetVolunteerQuery = GetVolunteerQuery.from_dict({"id": pk})
        volunteer: Volunteer = VolunteerService.get(query)

        if volunteer:
            return VolunteerSerializer(volunteer).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
