#  coding: utf-8
from core.cqrs import Validator, Field, Command


class CreateCityCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("state_id", "integer", True),

    ]

    def __init__(self, name: str, state_id: int):
        self.name = name
        self.state_id = state_id


    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateCityCommand':
        data = Validator.validate_and_extract(CreateCityCommand.fields, args)
        return CreateCityCommand(**data)


class PatchCityCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
        Field("state_id", "integer", True),
    ]

    def __init__(self, id: int, name: str = None, state_id: int = None):
        self.id = id
        self.name = name
        self.state_id = state_id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchCityCommand':
        data = Validator.validate_and_extract(PatchCityCommand.fields, args)
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
