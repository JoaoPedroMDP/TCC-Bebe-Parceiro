#  coding: utf-8
from datetime import timedelta
import logging
from typing import List

from config import PENDING, APPROVED
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand, PatchAppointmentCommand
from core.cqrs.queries.appointment_queries import GetAppointmentsReportQuery, ListAppointmentQuery
from core.models import Appointment
from core.repositories.appointment_repository import AppointmentRepository
from core.repositories.status_repository import StatusRepository
from core.services import CrudService

lgr = logging.getLogger(__name__)


class AppointmentService(CrudService):

    @classmethod
    def create(cls, command: CreateAppointmentCommand):
        if command.user.is_volunteer():
            command.status_id = StatusRepository.get_by_name(APPROVED).id
        else:
            command.status_id = StatusRepository.get_by_name(PENDING).id
        return AppointmentRepository.create(command.to_dict())

    @classmethod
    def patch(cls, command: PatchAppointmentCommand) -> Appointment:
        return AppointmentRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListAppointmentQuery) -> List[Appointment]:
        filters = query.to_dict()
        if 'status' in filters:
            # Me certifico de que o status passado existe
            statusId = StatusRepository.get_by_name(filters['status']).id
            filters['status_id'] = statusId
            filters.pop('status')

        return AppointmentRepository.filter(**filters)

    @classmethod
    def get(cls, query):
        return AppointmentRepository.get(query.id)

    @classmethod
    def delete(cls, command):
        return AppointmentRepository.delete(command.id)

    @classmethod
    def get_reports(cls, query: GetAppointmentsReportQuery):
        filters = {}
        if query.start_date:
            filters['datetime__gte'] = query.start_date
        
        if query.end_date:
            filters['datetime__lte'] = query.end_date + timedelta(days=1)

        return AppointmentRepository.filter(**filters)