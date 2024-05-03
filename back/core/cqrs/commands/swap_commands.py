#  coding: utf-8
from core.cqrs import Validator, Field, Command


class CreateSwapCommand(Command):
    fields = [
        Field("cloth_size", "object", True),
        Field("shoe_size", "object", False),
        Field("description", "string", False),
        Field("child", "object", True),
    ]

    def __init__(self, cloth_size: dict, shoe_size: dict = None, description: str = None, child: dict = None):
        self.cloth_size = cloth_size
        self.shoe_size = shoe_size
        self.description = description
        self.child = child

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateSwapCommand':
        data = Validator.validate_and_extract(CreateSwapCommand.fields, args)
        return CreateSwapCommand(**data)


class PatchSwapCommand(Command):
    fields = [
        Field("status", "object", False),
    ]

    def __init__(self, status: dict = None):
        self.status = status
    
    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchSwapCommand':
        data = Validator.validate_and_extract(PatchSwapCommand.fields, args)
        return PatchSwapCommand(**data)


class DeleteSwapCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteSwapCommand':
        data = Validator.validate_and_extract(DeleteSwapCommand.fields, args)
        return DeleteSwapCommand(**data)
