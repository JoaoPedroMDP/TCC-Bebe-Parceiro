#  coding: utf-8
from core.cqrs import Query, Field, Validator


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
