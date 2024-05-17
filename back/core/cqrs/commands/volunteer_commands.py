#  coding: utf-8
from typing import Dict, Optional

from core.cqrs import Validator, Field, Command


class CreateVolunteerCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("phone", "string", True),
        Field("email", "string", False),
        Field("password", "string", True),
        Field("group_ids", "list", True),
        Field("city_id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, name: str, phone: str, email: str, password: str, group_ids: list, city_id: int):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.group_ids = group_ids
        self.city_id = city_id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateVolunteerCommand':
        data = Validator.validate_and_extract(CreateVolunteerCommand.fields, args)
        return CreateVolunteerCommand(**data)


class PatchVolunteerCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
        Field("phone", "string", False),
        Field("email", "string", False),
        Field("password", "string", False),
        Field("group_ids", "list", False),
        Field("city_id", "integer", False, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int, group_ids: list, city_id: int, user_data: Dict = None):
        self.id = id
        self.group_ids = group_ids
        self.city_id = city_id
        self.user_data: Optional[Dict] = user_data


    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchVolunteerCommand':
        data = Validator.validate_and_extract(PatchVolunteerCommand.fields, args)
        data['user_data'] = Command.extract_and_group_keys(data, ["name", "phone", "password", "email"])
        return PatchVolunteerCommand(**data)


class DeleteVolunteerCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteVolunteerCommand':
        data = Validator.validate_and_extract(DeleteVolunteerCommand.fields, args)
        return DeleteVolunteerCommand(**data)
