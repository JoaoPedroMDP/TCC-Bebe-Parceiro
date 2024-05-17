#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from core.app_views import BaseView


from core.cqrs.commands.professional_commands import CreateProfessionalCommand, PatchProfessionalCommand, DeleteProfessionalCommand
from core.cqrs.queries.professional_queries import GetProfessionalQuery, ListProfessionalQuery
from core.models import Professional
from core.serializers import ProfessionalSerializer
from core.services.professional_service import ProfessionalService
from core.utils.decorators import endpoint
from config import MANAGE_PROFESSIONALS
from core.permissions.at_least_one_group import AtLeastOneGroup
from rest_framework.permissions import IsAuthenticated


lgr = logging.getLogger(__name__)


class ProfessionalGenericViews(BaseView):
    groups = [MANAGE_PROFESSIONALS]
    permission_classes = (IsAuthenticated,)
    permission_classes_by_method = {
        "post": (),
    }
    authentication_classes_by_method = {
        "post": (),
    }

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_PROFESSIONALS----")
        list_professionals_query: ListProfessionalQuery = ListProfessionalQuery.from_dict(request.query_params)
        professionals: List[Professional] = ProfessionalService.filter(list_professionals_query)
        return ProfessionalSerializer(professionals, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_PROFESSIONALS----")
        command: CreateProfessionalCommand = CreateProfessionalCommand.from_dict(request.data)
        
        if request.user.is_volunteer():
            command.approved = True
        
        new_professional: Professional = ProfessionalService.create(command)
        return ProfessionalSerializer(new_professional).data, status.HTTP_201_CREATED


class ProfessionalSpecificViews(BaseView):
    groups = [MANAGE_PROFESSIONALS]
    permission_classes = (AtLeastOneGroup,)
    permission_classes_by_method = {
    }
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_PROFESSIONALS----")
        data = copy(request.data)

        data['id'] = pk

        command: PatchProfessionalCommand = PatchProfessionalCommand.from_dict(data)
        patched_professional: Professional = ProfessionalService.patch(command)

        return ProfessionalSerializer(patched_professional).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_PROFESSIONAL----")
        command: DeleteProfessionalCommand = DeleteProfessionalCommand.from_dict({'id': int(pk)})
        deleted: bool = ProfessionalService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_PROFESSIONAL----")
        query: GetProfessionalQuery = GetProfessionalQuery.from_dict({"id": pk})
        professional: Professional = ProfessionalService.get(query)

        if professional:
            return ProfessionalSerializer(professional).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
