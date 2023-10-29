#  coding: utf-8
from core.cqrs import Validator, Field


class CreateAccessCodeCommand(Validator):
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
