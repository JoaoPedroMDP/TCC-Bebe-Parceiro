#  coding: utf-8
import logging
from typing import List

from config import PENDING, ROLE_BENEFICIARY, APPROVED, ROLE_VOLUNTEER
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand
from core.cqrs.queries.appointment_queries import ListAppointmentQuery
from core.models import Appointment
from core.repositories.appointment_repository import AppointmentRepository
from core.repositories.status_repository import StatusRepository
from core.services import CrudService

lgr = logging.getLogger(__name__)

class AppointmentService(CrudService):

    @classmethod
    def create(cls, command: CreateAppointmentCommand):
        if command.user.groups.filter(name=ROLE_VOLUNTEER).exists():
            command.status_id = StatusRepository.get_by_name(APPROVED).id
        else:
            command.status_id = StatusRepository.get_by_name(PENDING).id
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
