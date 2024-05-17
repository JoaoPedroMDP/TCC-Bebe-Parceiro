#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetSizeQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetSizeQuery':
        data = Validator.validate_and_extract(GetSizeQuery.fields, args)
        return GetSizeQuery(**data)


class ListSizeQuery(Query):
    fields = [
        Field("name", "string", False, formatter=lambda x: str(x)),
    ]

    def __init__(self, name: str = None):
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListSizeQuery':
        data = Validator.validate_and_extract(ListSizeQuery.fields, args)
        return ListSizeQuery(**data)
