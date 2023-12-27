#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetUserQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetUserQuery':
        data = Validator.validate_and_extract(GetUserQuery.fields, args)
        return GetUserQuery(**data)


class ListUserQuery(Query):
    fields = [
        Field("name", "string", False),
        Field("email", "string", False),
        Field("phone", "string", False),
        Field("password", "string", False),
    ]

    def __init__(self, name: str, phone: str, password: str, email: str = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListUserQuery':
        data = Validator.validate_and_extract(ListUserQuery.fields, args)
        return ListUserQuery(**data)
