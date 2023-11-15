#  coding: utf-8
from core.cqrs import Validator, Field, Command


class CreateCountryCommand(Command):
    fields = [
        Field("name", "string", True)
    ]

    def __init__(self, name: str):
        self.name = name


    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateCountryCommand':
        data = Validator.validate_and_extract(CreateCountryCommand.fields, args)
        return CreateCountryCommand(**data)


class PatchCountryCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False)
    ]

    def __init__(self, id: int, name: str = None):
        self.id = id
        self.name = name

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchCountryCommand':
        data = Validator.validate_and_extract(PatchCountryCommand.fields, args)
        return PatchCountryCommand(**data)


class DeleteCountryCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteCountryCommand':
        data = Validator.validate_and_extract(DeleteCountryCommand.fields, args)
        return DeleteCountryCommand(**data)
