#  coding: utf-8
from core.cqrs import Command, Field, Validator


class CreateUserCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("email", "string", False),
        Field("phone", "string", True),
        Field("password", "string", True),
    ]

    def __init__(self, name: str, phone: str, password: str, email: str = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateUserCommand':
        data = Validator.validate_and_extract(CreateUserCommand.fields, args)
        return CreateUserCommand(**data)


class PatchUserCommand(Command):
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
    def from_dict(args: dict) -> 'PatchUserCommand':
        data = Validator.validate_and_extract(PatchUserCommand.fields, args)
        return PatchUserCommand(**data)


class DeleteUserCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteUserCommand':
        data = Validator.validate_and_extract(DeleteUserCommand.fields, args)
        return DeleteUserCommand(**data)
