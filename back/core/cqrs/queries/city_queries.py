#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetCityQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetCityQuery':
        data = Validator.validate_and_extract(GetCityQuery.fields, args)
        return GetCityQuery(**data)


class ListCityQuery(Query):
    fields = [
        Field("enabled", "bool", False, formatter=lambda x: Validator.to_bool(x)),
        Field("state_id", "integer", False, formatter=lambda x: int(x)),
        Field("name", "string", False, formatter=lambda x: str(x)),
    ]

    def __init__(self, enabled: bool = None, state_id: int = None, name: str = None):
        self.enabled = enabled
        self.state_id = state_id
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListCityQuery':
        data = Validator.validate_and_extract(ListCityQuery.fields, args)
        return ListCityQuery(**data)
