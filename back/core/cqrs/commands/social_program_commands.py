#  coding: utf-8
from core.cqrs import Validator, Field, Command
from core.repositories.social_program_repository import SocialProgramRepository


def check_for_duplicity(data: dict):
    conflicts = SocialProgramRepository.filter(name=data['name'])
    if len(conflicts) > 0:
        raise AssertionError("Programa Social já cadastrado")


class CreateSocialProgramCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x), default=True)
    ]

    def __init__(self, name: str, enabled: bool):
        self.name = name
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateSocialProgramCommand':
        data = Validator.validate_and_extract(CreateSocialProgramCommand.fields, args)
        check_for_duplicity(data)
        return CreateSocialProgramCommand(**data)


class PatchSocialProgramCommand(Command):
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
    def from_dict(args: dict) -> 'PatchSocialProgramCommand':
        data = Validator.validate_and_extract(PatchSocialProgramCommand.fields, args)
        check_for_duplicity(data)
        return PatchSocialProgramCommand(**data)


class DeleteSocialProgramCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteSocialProgramCommand':
        data = Validator.validate_and_extract(DeleteSocialProgramCommand.fields, args)
        return DeleteSocialProgramCommand(**data)
