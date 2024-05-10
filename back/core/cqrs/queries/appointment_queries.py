#  coding: utf-8
from core.cqrs import Query, Field, Validator
from datetime import datetime

def format_date(raw_date: str):
    return datetime.strptime(raw_date, "%Y-%m-%d")


def format_time(raw_time: str):
    return datetime.strptime(raw_time, "%H:%M:%S")


class GetAppointmentQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetAppointmentQuery':
        data = Validator.validate_and_extract(GetAppointmentQuery.fields, args)
        return GetAppointmentQuery(**data)


class ListAppointmentQuery(Query):
    fields = [
        Field('beneficiary_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('volunteer_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('professional_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('speciality_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('status_id', 'integer', required=False, formatter=lambda x: int(x)),
        Field('date', datetime, required=False, formatter=format_date),
        Field('time', datetime, required=False, formatter=format_time),
    ]

    def __init__(self, beneficiary_id: int, date: datetime, time: datetime,
                 professional_id: int = None, volunteer_id: int = None, speciality_id: int = None, status_id: int = None
                 ):
        self.beneficiary_id = beneficiary_id
        self.date = date
        self.time = time
        self.professional_id = professional_id
        self.volunteer_id = volunteer_id
        self.speciality_id = speciality_id
        self.status_id = status_id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListAppointmentQuery':
        data = Validator.validate_and_extract(ListAppointmentQuery.fields, args)
        return ListAppointmentQuery(**data)
