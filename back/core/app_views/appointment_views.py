#  coding: utf-8
import logging
from copy import copy
from typing import List

from rest_framework import status
from rest_framework.request import Request

from config import MANAGE_APPOINTMENTS, MANAGE_REPORTS, MANAGE_EVALUATIONS
from core.app_views import BaseView
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand, EndEvaluationCommand, PatchAppointmentCommand, \
    DeleteAppointmentCommand
from core.cqrs.queries.appointment_queries import GetAppointmentQuery, GetAppointmentsReportQuery, ListAppointmentQuery
from core.models import Appointment
from core.permissions.at_least_one_group import AtLeastOneGroup
from core.permissions.is_volunteer import IsVolunteer
from core.serializers import AppointmentSerializer
from core.services.appointment_service import AppointmentService
from core.utils.decorators import endpoint
from rest_framework.permissions import IsAuthenticated

lgr = logging.getLogger(__name__)


class AppointmentGenericViews(BaseView):

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_ALL_APPOINTMENTS----")
        list_appointments_query: ListAppointmentQuery = ListAppointmentQuery.from_dict(request.query_params)
        list_appointments_query.user = request.user
        appointments: List[Appointment] = AppointmentService.filter(list_appointments_query)
        return AppointmentSerializer(appointments, many=True).data, status.HTTP_200_OK

    @endpoint
    def post(self, request: Request, format=None):
        lgr.debug("----CREATE_APPOINTMENT----")
        data = copy(request.data)
        command: CreateAppointmentCommand = CreateAppointmentCommand.from_dict(data)
        command.user = request.user
        new_appointment: Appointment = AppointmentService.create(command)
        return AppointmentSerializer(new_appointment).data, status.HTTP_201_CREATED


class AppointmentSpecificViews(BaseView):
    groups = [MANAGE_APPOINTMENTS]
    permission_classes = (AtLeastOneGroup,)
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


class AppointmentReportsView(BaseView):
    groups = [MANAGE_REPORTS]
    permission_classes = [IsAuthenticated, IsVolunteer, AtLeastOneGroup]

    @endpoint
    def get(self, request: Request, format=None):
        lgr.debug("----GET_APPOINTMENTS_REPORTS----")
        query: GetAppointmentsReportQuery = GetAppointmentsReportQuery.from_dict(request.query_params)
        appointments: List[Appointment] = AppointmentService.get_reports(query)
        return AppointmentSerializer(appointments, many=True).data, status.HTTP_200_OK


class ListAssignedEvaluationsViews(BaseView):
    groups = [MANAGE_EVALUATIONS]
    permission_classes = [IsAuthenticated, IsVolunteer, AtLeastOneGroup]

    @endpoint
    def get(self, request, format=None):
        lgr.debug("----GET_ASSIGNED_EVALUATIONS----")
        evaluations: List[Appointment] = AppointmentService.list_assigned_evaluations(request.user.volunteer.get().id)
        return AppointmentSerializer(evaluations, many=True).data, status.HTTP_200_OK


class EndEvaluationViews(BaseView):
    groups = [MANAGE_EVALUATIONS]
    permission_classes = [IsAuthenticated, IsVolunteer, AtLeastOneGroup]

    @endpoint
    def patch(self, request, pk, format=None):
        lgr.debug("----END_EVALUATION----")
        data = copy(request.data)
        data['id'] = pk

        command: EndEvaluationCommand = EndEvaluationCommand.from_dict(data)
        command.user = request.user
        evaluation: Appointment = AppointmentService.end_evaluation(command)

        return AppointmentSerializer(evaluation).data, status.HTTP_200_OK
