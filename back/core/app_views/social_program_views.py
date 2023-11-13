#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.social_program_commands import CreateSocialProgramCommand, PatchSocialProgramCommand, \
    DeleteSocialProgramCommand
from core.cqrs.queries.social_program_queries import GetSocialProgramQuery, ListSocialProgramQuery
from core.models import SocialProgram
from core.serializers import SocialProgramSerializer
from core.services.social_program_service import SocialProgramService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class SocialProgramGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_SOCIAL-PROGRAMS----")
        list_social_programs_query: ListSocialProgramQuery = ListSocialProgramQuery.from_dict(request.query_params)
        social_programs: List[SocialProgram] = SocialProgramService.list(list_social_programs_query)
        return SocialProgramSerializer(social_programs, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_SOCIAL-PROGRAM----")
        command: CreateSocialProgramCommand = CreateSocialProgramCommand.from_dict(request.data)
        new_social_program: SocialProgram = SocialProgramService.create(command)

        return SocialProgramSerializer(new_social_program).data, status.HTTP_201_CREATED


class SocialProgramSpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_SOCIAL-PROGRAM----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchSocialProgramCommand = PatchSocialProgramCommand.from_dict(data)
        patched_social_program: SocialProgram = SocialProgramService.patch(command)

        return SocialProgramSerializer(patched_social_program).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_SOCIAL-PROGRAM----")
        command: DeleteSocialProgramCommand = DeleteSocialProgramCommand.from_dict({'id': int(pk)})
        deleted: bool = SocialProgramService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_SOCIAL-PROGRAM----")
        query: GetSocialProgramQuery = GetSocialProgramQuery.from_dict({"id": pk})
        social_program: SocialProgram = SocialProgramService.get(query)
        if social_program:
            return SocialProgramSerializer(social_program).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
