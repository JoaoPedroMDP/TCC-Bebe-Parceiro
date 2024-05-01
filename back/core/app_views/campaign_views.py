#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request

from config import MANAGE_CAMPAIGNS
from core.app_views import BaseView
from core.cqrs.commands.campaign_commands import CreateCampaignCommand, PatchCampaignCommand, \
    DeleteCampaignCommand
from core.cqrs.queries.campaign_queries import GetCampaignQuery, ListCampaignQuery
from core.models import Campaign
from core.permissions.at_least_one_group import AtLeastOneGroup
from core.serializers import CampaignSerializer
from core.services.campaign_service import CampaignService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class CampaignGenericViews(BaseView):
    groups = [MANAGE_CAMPAIGNS]
    permission_classes = (AtLeastOneGroup,)
    permission_classes_by_method = {
        "get": ()
    }

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_CAMPAIGNS----")
        list_campaigns_query: ListCampaignQuery = ListCampaignQuery.from_dict(request.query_params)
        campaigns: List[Campaign] = CampaignService.filter(list_campaigns_query)
        return CampaignSerializer(campaigns, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_CAMPAIGN----")
        command: CreateCampaignCommand = CreateCampaignCommand.from_dict(request.data)
        new_campaign: Campaign = CampaignService.create(command)

        return CampaignSerializer(new_campaign).data, status.HTTP_201_CREATED


class CampaignSpecificViews(BaseView):
    groups = [MANAGE_CAMPAIGNS]
    permission_classes = (AtLeastOneGroup,)
    permission_classes_by_method = {
        "get": []
    }

    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_CAMPAIGN----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchCampaignCommand = PatchCampaignCommand.from_dict(data)
        patched_campaign: Campaign = CampaignService.patch(command)

        return CampaignSerializer(patched_campaign).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_CAMPAIGN----")
        command: DeleteCampaignCommand = DeleteCampaignCommand.from_dict({'id': int(pk)})
        deleted: bool = CampaignService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_CAMPAIGN----")
        query: GetCampaignQuery = GetCampaignQuery.from_dict({"id": pk})
        campaign: Campaign = CampaignService.get(query)

        if campaign:
            return CampaignSerializer(campaign).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
