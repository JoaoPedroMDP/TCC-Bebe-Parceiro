#  coding: utf-8
from core.cqrs import Validator, Field, Command


class CreateAccessCodeCommand(Command):
    fields = [
        Field("prefix", "string", True)
    ]

    def __init__(self, prefix: str):
        self.prefix = prefix

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateAccessCodeCommand':
        data = Validator.validate_and_extract(CreateAccessCodeCommand.fields, args)
        return CreateAccessCodeCommand(**data)


class PatchAccessCodeCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("used", "boolean", True, formatter=lambda x: bool(x))
    ]

    def __init__(self, id: int, used: bool):
        self.id = id
        self.used = used

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchAccessCodeCommand':
        data = Validator.validate_and_extract(PatchAccessCodeCommand.fields, args)
        return PatchAccessCodeCommand(**data)


class DeleteAccessCodeCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteAccessCodeCommand':
        data = Validator.validate_and_extract(DeleteAccessCodeCommand.fields, args)
        return DeleteAccessCodeCommand(**data)
