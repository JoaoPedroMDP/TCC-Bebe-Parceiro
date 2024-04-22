#  coding: utf-8
from config import PENDING
from core.cqrs.commands.appointment_commands import CreateAppointmentCommand
from core.repositories.appointment_repository import AppointmentRepository
from core.repositories.status_repository import StatusRepository
from core.services import CrudService


class AppointmentService(CrudService):

    @classmethod
    def create(cls, command: CreateAppointmentCommand):
        data = command.to_dict()
        status = StatusRepository.filter(name=PENDING)
        return AppointmentRepository.create(command.to_dict())

    def patch(self, command):
        return AppointmentRepository.patch(command.to_dict())

    def filter(self, query):
        return AppointmentRepository.filter(**query.to_dict())

    def get(self, query):
        return AppointmentRepository.get(query.id)

    def delete(self, command):
        return AppointmentRepository.delete(command.id)
