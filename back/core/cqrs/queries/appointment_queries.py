#  coding: utf-8
from core.cqrs import Query, Field, Validator


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
        Field("name", "string", False, formatter=lambda x: str(x)),
    ]

    def __init__(self, name: str = None):
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListAppointmentQuery':
        data = Validator.validate_and_extract(ListAppointmentQuery.fields, args)
        return ListAppointmentQuery(**data)
