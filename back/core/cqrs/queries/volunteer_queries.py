#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetVolunteerQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetVolunteerQuery':
        data = Validator.validate_and_extract(GetVolunteerQuery.fields, args)
        return GetVolunteerQuery(**data)


class ListVolunteerQuery(Query):
    fields = [
        Field("role_ids", "list", False),
        Field("city_id", "integer", False, formatter=lambda x: int(x)),
    ]

    def __init__(self, role_ids: list = None, city_id: int = None):
        self.role_ids = role_ids
        self.city_id = city_id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListVolunteerQuery':
        data = Validator.validate_and_extract(ListVolunteerQuery.fields, args)
        return ListVolunteerQuery(**data)
