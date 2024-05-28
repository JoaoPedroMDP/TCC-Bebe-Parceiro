#  coding: utf-8
from typing import Dict

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
        Field('beneficiary_id', 'integer',  False, formatter=lambda x: int(x)),
        Field('volunteer_id', 'integer', False, formatter=lambda x: int(x)),
        Field('professional_id', 'integer', False, formatter=lambda x: int(x)),
        Field('speciality_id', 'integer', False, formatter=lambda x: int(x)),
        Field('status_id', 'integer', False, formatter=lambda x: int(x)),
        Field('datetime', 'string', required=False),
        Field('status', 'string', False)
    ]

    def __init__(self, beneficiary_id: int = None, volunteer_id: int = None, professional_id: int = None, speciality_id: int = None, status_id: int = None,
                 datetime: str = None, status: str = None
                 ):
        self.beneficiary_id = beneficiary_id
        self.datetime = datetime
        self.professional_id = professional_id
        self.volunteer_id = volunteer_id
        self.speciality_id = speciality_id
        self.status_id = status_id
        self.status = status
        self.user = None
    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListAppointmentQuery':
        data = Validator.validate_and_extract(ListAppointmentQuery.fields, args)
        return ListAppointmentQuery(**data)

    def to_dict(self) -> Dict:
        data = super().to_dict()
        del data['user']
        return data

class GetAppointmentsReportQuery(Query):
    fields = [
        Field("start_date", "string", False),
        Field("end_date", "string", False),
    ]

    def __init__(self, start_date: datetime = None, end_date: datetime = None):
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetAppointmentsReportQuery':
        data = Validator.validate_and_extract(GetAppointmentsReportQuery.fields, args)

        if 'start_date' in data:
            data['start_date'] = datetime.fromisoformat(data['start_date'])

        if 'end_date' in data:
            data['end_date'] = datetime.fromisoformat(data['end_date'])

        return GetAppointmentsReportQuery(**data)
    