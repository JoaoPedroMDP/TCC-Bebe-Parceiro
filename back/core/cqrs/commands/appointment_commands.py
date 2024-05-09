#  coding: utf-8
from datetime import datetime
from typing import Dict

from core.cqrs import Command, Field, Validator
from core.repositories.appointment_repository import AppointmentRepository


def format_date(raw_date: str):
    return datetime.strptime(raw_date, "%Y-%m-%d")


def format_time(raw_time: str):
    return datetime.strptime(raw_time, "%H:%M:%S")


class CreateAppointmentCommand(Command):
    fields = [
        Field('beneficiary_id', 'integer', required=True, formatter=lambda x: int(x)),
        Field('volunteer_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('professional_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('date', datetime, required=True, formatter=format_date),
        Field('time', datetime, required=True, formatter=format_time),
    ]

    def __init__(self, beneficiary_id: int, date: datetime, time: datetime,
                 professional_id: int = None, volunteer_id: int = None
                 ):
        self.beneficiary_id = beneficiary_id
        self.date = date
        self.time = time
        self.professional_id = professional_id
        self.volunteer_id = volunteer_id

    @staticmethod
    @Validator.validates
    def from_dict(args: Dict):
        data = Validator.validate_and_extract(CreateAppointmentCommand.fields, args)
        return CreateAppointmentCommand(**data)

class PatchAppointmentCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
    ]

    def __init__(self, id: int, name: str = None):
        self.id = id
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchAppointmentCommand':
        data = Validator.validate_and_extract(PatchAppointmentCommand.fields, args)
        return PatchAppointmentCommand(**data)


class DeleteAppointmentCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteAppointmentCommand':
        data = Validator.validate_and_extract(DeleteAppointmentCommand.fields, args)
        return DeleteAppointmentCommand(**data)
