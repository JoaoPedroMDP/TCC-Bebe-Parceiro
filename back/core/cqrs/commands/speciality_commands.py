#  coding: utf-8
from core.cqrs import Validator, Field, Command
from core.repositories.speciality_repository import SpecialityRepository


def check_for_duplicity(data: dict):
    conflicts = SpecialityRepository.filter(name=data['name'])
    if len(conflicts) > 0:
        raise AssertionError("Especialidade já cadastrada")


class CreateSpecialityCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x), default=True)
    ]

    def __init__(self, name: str, enabled: bool):
        self.name = name
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateSpecialityCommand':
        data = Validator.validate_and_extract(CreateSpecialityCommand.fields, args)
        check_for_duplicity(data)
        return CreateSpecialityCommand(**data)


class PatchSpecialityCommand(Command):
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
    def from_dict(args: dict) -> 'PatchSpecialityCommand':
        data = Validator.validate_and_extract(PatchSpecialityCommand.fields, args)
        check_for_duplicity(data)
        return PatchSpecialityCommand(**data)


class DeleteSpecialityCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteSpecialityCommand':
        data = Validator.validate_and_extract(DeleteSpecialityCommand.fields, args)
        return DeleteSpecialityCommand(**data)
