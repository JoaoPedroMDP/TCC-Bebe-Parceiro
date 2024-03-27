#  coding: utf-8
from core.cqrs import Query, Field, Validator


class CheckAccessCodeQuery(Query):
    fields = [
        Field("code", "string", True),
    ]

    def __init__(self, code: str):
        self.code = code

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CheckAccessCodeQuery':
        data = Validator.validate_and_extract(CheckAccessCodeQuery.fields, args)
        return CheckAccessCodeQuery(**data)


class GetAccessCodeQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetAccessCodeQuery':
        data = Validator.validate_and_extract(GetAccessCodeQuery.fields, args)
        return GetAccessCodeQuery(**data)


class ListAccessCodeQuery(Query):
    fields = [
        Field("code", "string", False, formatter=lambda x: str(x)),
        Field("used", "bool", False, formatter=lambda x: Validator.to_bool(x)),
    ]

    def __init__(self, used: bool = None, code: str = None):
        self.used = used
        self.code = code

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListAccessCodeQuery':
        data = Validator.validate_and_extract(ListAccessCodeQuery.fields, args)
        return ListAccessCodeQuery(**data)
