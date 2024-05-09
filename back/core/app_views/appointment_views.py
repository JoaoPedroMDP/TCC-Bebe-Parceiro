#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request

from core.app_views import BaseView
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand, PatchAppointmentCommand, \
    DeleteAppointmentCommand
from core.cqrs.queries.appointment_queries import GetAppointmentQuery, ListAppointmentQuery
from core.models import Appointment
from core.serializers import AppointmentSerializer
from core.services.appointment_service import AppointmentService
from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


class AppointmentGenericViews(BaseView):
    authentication_classes_by_method = {
        "get": ()
    }
    permission_classes_by_method = {
        "get": ()
    }

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_APPOINTMENTS----")
        list_appointments_query: ListAppointmentQuery = ListAppointmentQuery.from_dict(request.query_params)
        appointments: List[Appointment] = AppointmentService.filter(list_appointments_query)
        return AppointmentSerializer(appointments, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_APPOINTMENT----")
        command: CreateAppointmentCommand = CreateAppointmentCommand.from_dict(request.data)
        new_appointment: Appointment = AppointmentService.create(command)

        return AppointmentSerializer(new_appointment).data, status.HTTP_201_CREATED


class AppointmentSpecificViews(BaseView):
    @endpoint
    def patch(self, request: Request, pk, format=None):
        lgr.debug("----PATCH_APPOINTMENT----")
        data = copy(request.data)
        data['id'] = pk

        command: PatchAppointmentCommand = PatchAppointmentCommand.from_dict(data)
        patched_appointment: Appointment = AppointmentService.patch(command)

        return AppointmentSerializer(patched_appointment).data, status.HTTP_200_OK

    @endpoint
    def delete(self, request: Request, pk, format=None):
        lgr.debug("----DELETE_APPOINTMENT----")
        command: DeleteAppointmentCommand = DeleteAppointmentCommand.from_dict({'id': int(pk)})
        deleted: bool = AppointmentService.delete(command)

        if deleted:
            return {}, status.HTTP_204_NO_CONTENT

        return {}, status.HTTP_404_NOT_FOUND

    @endpoint
    def get(self, request: Request, pk, format=None):
        lgr.debug("----GET_APPOINTMENT----")
        query: GetAppointmentQuery = GetAppointmentQuery.from_dict({"id": pk})
        appointment: Appointment = AppointmentService.get(query)

        if appointment:
            return AppointmentSerializer(appointment).data, status.HTTP_200_OK

        return {}, status.HTTP_404_NOT_FOUND
