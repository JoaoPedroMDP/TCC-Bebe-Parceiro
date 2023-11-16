#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetStateQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetStateQuery':
        data = Validator.validate_and_extract(GetStateQuery.fields, args)
        return GetStateQuery(**data)


class ListStateQuery(Query):
    fields = [
        Field("enabled", "bool", False, formatter=lambda x: Validator.to_bool(x)),
        Field("country_id", "integer", False),
    ]

    def __init__(self, enabled: bool = None, country_id: int = None,):
        self.enabled = enabled
        self.country_id = country_id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListStateQuery':
        data = Validator.validate_and_extract(ListStateQuery.fields, args)
        return ListStateQuery(**data)
