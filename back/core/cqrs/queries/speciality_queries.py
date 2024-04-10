#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetSpecialityQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetSpecialityQuery':
        data = Validator.validate_and_extract(GetSpecialityQuery.fields, args)
        return GetSpecialityQuery(**data)


class ListSpecialityQuery(Query):
    fields = [
        Field("enabled", "bool", False, formatter=lambda x: Validator.to_bool(x)),
        Field("name", "string", False, formatter=lambda x: str(x)),
    ]

    def __init__(self, enabled: bool = None, name: str = None):
        self.enabled = enabled
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListSpecialityQuery':
        data = Validator.validate_and_extract(ListSpecialityQuery.fields, args)
        return ListSpecialityQuery(**data)
