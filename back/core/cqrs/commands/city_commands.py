#  coding: utf-8
from core.cqrs import Validator, Field, Command
from core.repositories.city_repository import CityRepository


def check_for_duplicity(data: dict):
    conflicts = CityRepository.filter(state_id=data['state_id'], name=data['name'])
    if len(conflicts) > 0:
        raise AssertionError("Cidade já cadastrada")


class CreateCityCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("state_id", "integer", True, formatter=lambda x: int(x)),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x), default=True)
    ]

    def __init__(self, name: str, state_id: int, enabled: bool):
        self.name = name
        self.state_id = state_id
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateCityCommand':
        data = Validator.validate_and_extract(CreateCityCommand.fields, args)
        check_for_duplicity(data)
        return CreateCityCommand(**data)


class PatchCityCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
        Field("state_id", "integer", True, formatter=lambda x: int(x)),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x))
    ]

    def __init__(self, id: int, name: str = None, state_id: int = None, enabled: bool = None):
        self.id = id
        self.name = name
        self.state_id = state_id
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchCityCommand':
        data = Validator.validate_and_extract(PatchCityCommand.fields, args)
        check_for_duplicity(data)
        return PatchCityCommand(**data)


class DeleteCityCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteCityCommand':
        data = Validator.validate_and_extract(DeleteCityCommand.fields, args)
        return DeleteCityCommand(**data)
