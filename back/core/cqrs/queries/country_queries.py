#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetCountryQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetCountryQuery':
        data = Validator.validate_and_extract(GetCountryQuery.fields, args)
        return GetCountryQuery(**data)


class ListCountryQuery(Query):
    fields = [
        Field("enabled", "bool", False, formatter=lambda x: Validator.to_bool(x)),
    ]

    def __init__(self, enabled: bool = None):
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListCountryQuery':
        data = Validator.validate_and_extract(ListCountryQuery.fields, args)
        return ListCountryQuery(**data)
