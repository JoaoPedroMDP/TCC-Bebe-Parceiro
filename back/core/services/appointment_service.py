#  coding: utf-8
from typing import List

from config import PENDING, ROLE_BENEFICIARY, APPROVED
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand
from core.cqrs.queries.appointment_queries import ListAppointmentQuery
from core.models import Appointment
from core.repositories.appointment_repository import AppointmentRepository
from core.repositories.status_repository import StatusRepository
from core.services import CrudService


class AppointmentService(CrudService):

    @classmethod
    def create(cls, command: CreateAppointmentCommand):
        if command.user.is_volunteer():
            command.status_id = StatusRepository.get_by_name(APPROVED)
        else:
            command.status_id = StatusRepository.get_by_name(PENDING)
        return AppointmentRepository.create(command.to_dict())

    @classmethod
    def patch(cls, command):
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
