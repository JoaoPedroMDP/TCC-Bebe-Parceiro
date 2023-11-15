#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetSocialProgramQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetSocialProgramQuery':
        data = Validator.validate_and_extract(GetSocialProgramQuery.fields, args)
        return GetSocialProgramQuery(**data)


class ListSocialProgramQuery(Query):
    fields = [
        Field("enabled", "bool", False, formatter=lambda x: Validator.to_bool(x)),
    ]

    def __init__(self, enabled: bool = None):
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListSocialProgramQuery':
        data = Validator.validate_and_extract(ListSocialProgramQuery.fields, args)
        return ListSocialProgramQuery(**data)
