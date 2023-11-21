#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from core.cqrs.commands.country_commands import CreateCountryCommand, PatchCountryCommand, \
    DeleteCountryCommand
from core.cqrs.queries.country_queries import GetCountryQuery, ListCountryQuery
from core.db_models.adress_related_models import Country
from core.serializers import CountrySerializer
from core.services.country_service import CountryService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class CountryGenericViews(APIView):
    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_COUNTRIES----")
        list_countries_query: ListCountryQuery = ListCountryQuery.from_dict(request.query_params)
        countries: List[Country] = CountryService.filter(list_countries_query)
        return CountrySerializer(countries, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_COUNTRY----")
        command: CreateCountryCommand = CreateCountryCommand.from_dict(request.data)
        new_country: Country = CountryService.create(command)

        return CountrySerializer(new_country).data, status.HTTP_201_CREATED


class CountrySpecificViews(APIView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_COUNTRY----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchCountryCommand = PatchCountryCommand.from_dict(data)
        patched_country: Country = CountryService.patch(command)

        return CountrySerializer(patched_country).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_COUNTRY----")
        command: DeleteCountryCommand = DeleteCountryCommand.from_dict({'id': int(pk)})
        deleted: bool = CountryService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_COUNTRY----")
        query: GetCountryQuery = GetCountryQuery.from_dict({"id": pk})
        country: Country = CountryService.get(query)

        if country:
            return CountrySerializer(country).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
