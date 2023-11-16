#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.state_commands import CreateStateCommand, PatchStateCommand, \
    DeleteStateCommand
from core.cqrs.queries.state_queries import GetStateQuery, ListStateQuery
from core.db_models.adress_related_models import State
from core.serializers import StateSerializer
from core.services.state_service import StateService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class StateGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_STATES----")
        list_states_query: ListStateQuery = ListStateQuery.from_dict(request.query_params)
        states: List[State] = StateService.list(list_states_query)
        return StateSerializer(states, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_STATE----")
        command: CreateStateCommand = CreateStateCommand.from_dict(request.data)
        new_State: State = StateService.create(command)

        return StateSerializer(new_State).data, status.HTTP_201_CREATED


class StateSpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_STATES----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchStateCommand = PatchStateCommand.from_dict(data)
        patched_State: State = StateService.patch(command)

        return StateSerializer(patched_State).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_STATE----")
        command: DeleteStateCommand = DeleteStateCommand.from_dict({'id': int(pk)})
        deleted: bool = StateService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_STATE----")
        query: GetStateQuery = GetStateQuery.from_dict({"id": pk})
        state: State = StateService.get(query)
        if State:
            return StateSerializer(State).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
