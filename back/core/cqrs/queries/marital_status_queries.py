#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetMaritalStatusQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetMaritalStatusQuery':
        data = Validator.validate_and_extract(GetMaritalStatusQuery.fields, args)
        return GetMaritalStatusQuery(**data)


class ListMaritalStatusQuery(Query):
    fields = [
        Field("enabled", "bool", False, formatter=lambda x: Validator.to_bool(x)),
        Field("name", "string", False),
    ]

    def __init__(self, enabled: bool = None, name: str = None):
        self.enabled = enabled
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListMaritalStatusQuery':
        data = Validator.validate_and_extract(ListMaritalStatusQuery.fields, args)
        return ListMaritalStatusQuery(**data)
