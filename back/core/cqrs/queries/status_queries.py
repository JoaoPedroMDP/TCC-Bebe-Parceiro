#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetStatusQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetStatusQuery':
        data = Validator.validate_and_extract(GetStatusQuery.fields, args)
        return GetStatusQuery(**data)


class ListStatusQuery(Query):
    fields = [
        Field("enabled", "bool", False, formatter=lambda x: Validator.to_bool(x)),
        Field("name", "string", False, formatter=lambda x: str(x)),
    ]

    def __init__(self, enabled: bool = None, name: str = None):
        self.enabled = enabled
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListStatusQuery':
        data = Validator.validate_and_extract(ListStatusQuery.fields, args)
        return ListStatusQuery(**data)
