#  coding: utf-8
from core.cqrs import Command, Field, Validator
from core.repositories.user_repository import UserRepository


def check_for_duplicity(data: dict, allowed_conflicts: int = 0):
    if 'email' in data:
        conflicts = UserRepository.filter(email=data['email'])
        if len(conflicts) > allowed_conflicts:
            raise AssertionError("Email já cadastrado")

    conflicts = UserRepository.filter(phone=data['phone'])
    if len(conflicts) > allowed_conflicts:
        raise AssertionError("Telefone já cadastrado")


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
        check_for_duplicity(data)
        return CreateUserCommand(**data)


class PatchUserCommand(Command):
    fields = [
        Field("id", "integer", True),
        Field("name", "string", False),
        Field("email", "string", False),
        Field("phone", "string", False),
        Field("password", "string", False),
    ]

    def __init__(self, id: int, name: str = None, phone: str = None, password: str = None, email: str = None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchUserCommand':
        data = Validator.validate_and_extract(PatchUserCommand.fields, args)
        check_for_duplicity(data, allowed_conflicts=1)
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
