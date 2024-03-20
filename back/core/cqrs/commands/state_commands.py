#  coding: utf-8
from core.cqrs import Validator, Field, Command
from core.repositories.state_repository import StateRepository


def check_for_duplicity(data: dict):
    conflicts = StateRepository.filter(name=data['name'], country_id=data['country_id'])
    if len(conflicts) > 0:
        raise AssertionError("Estado já cadastrado")


class CreateStateCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("country_id", "integer", True, formatter=lambda x: int(x)),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x), default=True)
    ]

    def __init__(self, name: str, country_id: int, enabled: bool):
        self.name = name
        self.country_id = country_id
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateStateCommand':
        data = Validator.validate_and_extract(CreateStateCommand.fields, args)
        check_for_duplicity(data)
        return CreateStateCommand(**data)


class PatchStateCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
        Field("country_id", "integer", True, formatter=lambda x: int(x)),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x))
    ]

    def __init__(self, id: int, name: str = None, country_id: int = None, enabled: bool = None):
        self.id = id
        self.name = name
        self.country_id = country_id
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchStateCommand':
        data = Validator.validate_and_extract(PatchStateCommand.fields, args)
        check_for_duplicity(data)
        return PatchStateCommand(**data)


class DeleteStateCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteStateCommand':
        data = Validator.validate_and_extract(DeleteStateCommand.fields, args)
        return DeleteStateCommand(**data)
