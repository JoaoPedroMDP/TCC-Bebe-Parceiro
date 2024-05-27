#  coding: utf-8
from core.cqrs import Validator, Field, Command

class CreateRegisterCommand(Command):
    fields = [
        Field("description", "string", True)
    ]

    def __init__(self, description: str):
        self.description = description

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateRegisterCommand':
        data = Validator.validate_and_extract(CreateRegisterCommand.fields, args)
        return CreateRegisterCommand(**data)


class PatchRegisterCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("description", "string", False)
    ]

    def __init__(self, id: int, description: str = None):
        self.id = id
        self.description = description

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchRegisterCommand':
        data = Validator.validate_and_extract(PatchRegisterCommand.fields, args)
        return PatchRegisterCommand(**data)


class DeleteRegisterCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteRegisterCommand':
        data = Validator.validate_and_extract(DeleteRegisterCommand.fields, args)
        return DeleteRegisterCommand(**data)
