#  coding: utf-8
from core.cqrs import Validator, Field, Command
from core.repositories.country_repository import CountryRepository


def check_for_duplicity(data: dict):
    conflicts = CountryRepository.filter(name=data['name'])
    if len(conflicts) > 0:
        raise AssertionError("País já cadastrado")


class CreateCountryCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("enabled", "boolean", False, formatter=lambda x: Validator.to_bool(x), default=True)
    ]

    def __init__(self, name: str, enabled: bool):
        self.name = name
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateCountryCommand':
        data = Validator.validate_and_extract(CreateCountryCommand.fields, args)
        check_for_duplicity(data)
        return CreateCountryCommand(**data)


class PatchCountryCommand(Command):
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
    def from_dict(args: dict) -> 'PatchCountryCommand':
        data = Validator.validate_and_extract(PatchCountryCommand.fields, args)
        check_for_duplicity(data)
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
