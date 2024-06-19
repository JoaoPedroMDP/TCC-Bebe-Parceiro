#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status as http_status
from rest_framework.request import Request

from core.app_views import BaseView
from core.cqrs.queries.status_queries import GetStatusQuery, ListStatusQuery
from core.models import Status
from core.serializers import StatusSerializer
from core.services.status_service import StatusService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class StatusGenericViews(BaseView):

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_STATUS----")
        list_status_query: ListStatusQuery = ListStatusQuery.from_dict(request.query_params)
        status: List[Status] = StatusService.filter(list_status_query)
        return StatusSerializer(status, many=True).data, http_status.HTTP_200_OK


class StatusSpecificViews(BaseView):

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_STATUS----")
        query: GetStatusQuery = GetStatusQuery.from_dict({"id": pk})
        status: Status = StatusService.get(query)

        if status:
            return StatusSerializer(status).data, http_status.HTTP_200_OK

        return {}, http_status.HTTP_404_NOT_FOUND
