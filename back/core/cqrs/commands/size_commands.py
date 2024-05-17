#  coding: utf-8
from core.cqrs import Validator, Field, Command
from core.repositories.size_repository import SizeRepository


def check_for_duplicity(data: dict):
    conflicts = SizeRepository.filter(name=data['name'])
    if len(conflicts) > 0:
        raise AssertionError("País já cadastrado")


class CreateSizeCommand(Command):
    fields = [
        Field("name", "string", True)
    ]

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateSizeCommand':
        data = Validator.validate_and_extract(CreateSizeCommand.fields, args)
        check_for_duplicity(data)
        return CreateSizeCommand(**data)


class PatchSizeCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
    ]

    def __init__(self, id: int, name: str = None):
        self.id = id
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchSizeCommand':
        data = Validator.validate_and_extract(PatchSizeCommand.fields, args)
        check_for_duplicity(data)
        return PatchSizeCommand(**data)


class DeleteSizeCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteSizeCommand':
        data = Validator.validate_and_extract(DeleteSizeCommand.fields, args)
        return DeleteSizeCommand(**data)
