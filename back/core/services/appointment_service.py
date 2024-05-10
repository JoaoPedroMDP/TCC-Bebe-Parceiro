#  coding: utf-8
from config import PENDING, ROLE_BENEFICIARY, APPROVED
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand
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

    def patch(self, command):
        return AppointmentRepository.patch(command.to_dict())

    def filter(self, query):
        return AppointmentRepository.filter(**query.to_dict())

    def get(self, query):
        return AppointmentRepository.get(query.id)

    def delete(self, command):
        return AppointmentRepository.delete(command.id)
