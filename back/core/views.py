#  coding: utf-8
import logging
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.access_code_commands import CreateAccessCodeCommand
from core.models import AccessCode
from core.serializers import AccessCodeSerializer
from core.services.AccessCodeService import AccessCodeService
from core.utils.decorators import endpoint


lgr = logging.getLogger(__name__)


class AccessCodeGenericView(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_TICKETCONFIGS----")
        access_codes: List[AccessCode] = AccessCodeService.list()
        return AccessCodeSerializer(access_codes, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_TICKETCONFIG----")
        command: CreateAccessCodeCommand = CreateAccessCodeCommand.from_dict(request.data)
        new_access_code: AccessCode = AccessCodeService.create(command)

        return AccessCodeSerializer(new_access_code).data, status.HTTP_201_CREATED
