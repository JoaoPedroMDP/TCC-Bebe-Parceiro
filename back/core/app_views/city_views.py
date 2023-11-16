#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.city_commands import CreateCityCommand, PatchCityCommand, \
    DeleteCityCommand
from core.cqrs.queries.city_queries import GetCityQuery, ListCityQuery
from core.db_models.adress_related_models import City
from core.serializers import CitySerializer
from core.services.city_service import CityService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class CityGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_CityS----")
        list_cities_query: ListCityQuery = ListCityQuery.from_dict(request.query_params)
        cities: List[City] = CityService.list(list_cities_query)
        return CitySerializer(cities, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_CITIES----")
        command: CreateCityCommand = CreateCityCommand.from_dict(request.data)
        new_City: City = CityService.create(command)

        return CitySerializer(new_City).data, status.HTTP_201_CREATED


class CitySpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_CITIES----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchCityCommand = PatchCityCommand.from_dict(data)
        patched_City: City = CityService.patch(command)

        return CitySerializer(patched_City).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_CITIES----")
        command: DeleteCityCommand = DeleteCityCommand.from_dict({'id': int(pk)})
        deleted: bool = CityService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_CITIES----")
        query: GetCityQuery = GetCityQuery.from_dict({"id": pk})
        city: City = CityService.get(query)
        if City:
            return CitySerializer(City).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
