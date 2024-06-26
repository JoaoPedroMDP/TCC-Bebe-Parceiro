#  coding: utf-8
from datetime import datetime
import logging
from typing import Dict

from core.cqrs import Command, Field, Validator
from core.models import User
from core.utils.exceptions import ValidationErrors


lgr = logging.getLogger(__name__)


def format_date(raw_date: str):
    return datetime.strptime(raw_date, "%Y-%m-%d")


def format_time(raw_time: str):
    return datetime.strptime(raw_time, "%H:%M:%S")


class CreateAppointmentCommand(Command):
    fields = [
        Field('beneficiary_id', 'integer', required=True, formatter=lambda x: int(x)),
        Field('volunteer_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('professional_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('speciality_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('datetime', 'string', required=False),
    ]

    def __init__(self, beneficiary_id: int, datetime: str = None,
                 professional_id: int = None, volunteer_id: int = None, speciality_id: int = None
                 ):
        self.beneficiary_id = beneficiary_id
        self.datetime = datetime
        self.professional_id = professional_id
        self.volunteer_id = volunteer_id
        self.speciality_id = speciality_id
        self.status_id = None
        self.user = None

    @staticmethod
    @Validator.validates
    def from_dict(args: Dict):
        data = Validator.validate_and_extract(CreateAppointmentCommand.fields, args)


        if 'volunteer_id' in data:
            if 'professional_id' in data or 'speciality_id' in data:
                raise ValueError("Um atendimento com voluntária não pode ter profissional nem especialidade")
        elif 'professional_id' not in data and 'speciality_id' not in data:
            raise ValueError("Um atendimento deve ter um profissional e uma especialidade, ou ser feito por uma voluntária")    

        return CreateAppointmentCommand(**data)


class PatchAppointmentCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field('beneficiary_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('volunteer_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('professional_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('speciality_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('status_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('datetime', 'string', required=False),
    ]

    def __init__(self, id: int, beneficiary_id: int = None, datetime: str = None,
                 professional_id: int = None, volunteer_id: int = None, speciality_id: int = None, status_id: int = None
                 ):
        self.id = id
        self.beneficiary_id = beneficiary_id
        self.datetime = datetime
        self.professional_id = professional_id
        self.volunteer_id = volunteer_id
        self.speciality_id = speciality_id
        self.status_id = status_id

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


class EndEvaluationCommand(Command):
    fields = [
        Field('id', 'integer', required=True, formatter=lambda x: int(x)),
        Field('description', 'string', required=True),
    ]

    def __init__(self, id: int, description: str):
        self.id = id
        self.description = description
        self.user: User = None

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'EndEvaluationCommand':
        data = Validator.validate_and_extract(EndEvaluationCommand.fields, args)
        return EndEvaluationCommand(**data)
