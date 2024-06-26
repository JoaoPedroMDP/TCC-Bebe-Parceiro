#  coding: utf-8
from core.cqrs import Validator, Field, Command
from core.repositories.marital_status_repository import MaritalStatusRepository


def check_for_duplicity(data: dict):
    conflicts = MaritalStatusRepository.filter(name=data['name'])
    if len(conflicts) > 0:
        raise AssertionError("Estado Civil já cadastrado")


class CreateMaritalStatusCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x), default=True)
    ]

    def __init__(self, name: str, enabled: bool):
        self.name = name
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateMaritalStatusCommand':
        data = Validator.validate_and_extract(CreateMaritalStatusCommand.fields, args)
        check_for_duplicity(data)
        return CreateMaritalStatusCommand(**data)


class PatchMaritalStatusCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x))
    ]

    def __init__(self, id: int, name: str = None, enabled: bool = None):
        self.id = id
        self.name = name
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchMaritalStatusCommand':
        data = Validator.validate_and_extract(PatchMaritalStatusCommand.fields, args)
        check_for_duplicity(data)
        return PatchMaritalStatusCommand(**data)


class DeleteMaritalStatusCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteMaritalStatusCommand':
        data = Validator.validate_and_extract(DeleteMaritalStatusCommand.fields, args)
        return DeleteMaritalStatusCommand(**data)
