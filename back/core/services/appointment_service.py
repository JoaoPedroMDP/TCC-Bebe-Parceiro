#  coding: utf-8
import logging
from typing import List

from config import PENDING, APPROVED
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand, EndEvaluationCommand, PatchAppointmentCommand
from core.cqrs.commands.register_commands import CreateRegisterCommand
from core.cqrs.queries.appointment_queries import ListAppointmentQuery
from core.models import Appointment, Register
from core.repositories.appointment_repository import AppointmentRepository
from core.repositories.status_repository import StatusRepository
from core.services import CrudService
from core.services.register_service import RegisterService
from core.utils.exceptions import HttpFriendlyError

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
        return AppointmentRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query):
        return AppointmentRepository.get(query.id)

    @classmethod
    def delete(cls, command):
        return AppointmentRepository.delete(command.id)

    @classmethod
    def list_assigned_evaluations(cls, volunteer_id: int):
        return AppointmentRepository.filter(volunteer_id=volunteer_id)

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
