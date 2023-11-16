#  coding: utf-8
from core.cqrs import Validator, Field, Command


class CreateStateCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("country_id", "integer", True),

    ]

    def __init__(self, name: str, country_id: int):
        self.name = name
        self.country_id = country_id


    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateStateCommand':
        data = Validator.validate_and_extract(CreateStateCommand.fields, args)
        return CreateStateCommand(**data)


class PatchStateCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
        Field("country_id", "integer", True),
    ]

    def __init__(self, id: int, name: str = None, country_id: int = None):
        self.id = id
        self.name = name
        self.country_id = country_id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchStateCommand':
        data = Validator.validate_and_extract(PatchStateCommand.fields, args)
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
