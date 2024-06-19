#  coding: utf-8
from datetime import timedelta
import logging
from typing import List

from config import FINISHED, PENDING, APPROVED
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand, EndEvaluationCommand, PatchAppointmentCommand
from core.cqrs.queries.appointment_queries import GetAppointmentsReportQuery, ListAppointmentQuery
from core.cqrs.commands.register_commands import CreateRegisterCommand
from core.models import Appointment, Status
from core.repositories.appointment_repository import AppointmentRepository
from core.repositories.status_repository import StatusRepository
from core.services import CrudService
from core.services.register_service import RegisterService

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

        if query.user.is_beneficiary():
           lgr.debug("Usuária é beneficiária")
           filters = {
                **filters,
                "beneficiary": query.user.beneficiary
            }

        if 'status' in filters:
            # Me certifico de que o status passado existe
            status = filters.pop('status')
            statusId = StatusRepository.get_by_name(status).id
            filters['status_id'] = statusId
        elif 'status_list' in filters:
            status_list = filters.pop('status_list')
            ids = [StatusRepository.get_by_name(x).id for x in status_list]
            filters['status_id__in'] = ids

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

    @classmethod
    def list_assigned_evaluations(cls, volunteer_id: int):
        status: Status = StatusRepository.get_by_name(APPROVED)
        return AppointmentRepository.filter(
            volunteer_id=volunteer_id,
            status_id=status.id
        )

    @classmethod
    def end_evaluation(cls, command: EndEvaluationCommand):
        appointment: Appointment = AppointmentRepository.get(command.id)

        reg_comm: CreateRegisterCommand = CreateRegisterCommand.from_dict({
            "appointment_id": appointment.id,
            "volunteer_id": command.user.volunteer.get().id,
            "beneficiary_id": appointment.beneficiary.id,
            "description": command.description
        })

        RegisterService.create(reg_comm)

        status: Status = StatusRepository.get_by_name(FINISHED)
        
        appo_command: PatchAppointmentCommand = PatchAppointmentCommand.from_dict({
            "id": appointment.id,
            "status_id": status.id
        })
        cls.patch(appo_command)

        appointment.refresh_from_db()
        return appointment
