#  coding: utf-8
from datetime import datetime

from core.cqrs import Validator, Field, Command


class CreateChildCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("beneficiary_id", "integer", True, formatter=lambda x: int(x)),
        Field("sex", "string", True),

        Field("birth_date", "string", False),
    ]

    def __init__(self, name: str, birth_date: str, beneficiary_id: int, sex: str):
        self.name = name
        self.birth_date = birth_date
        self.beneficiary_id = beneficiary_id
        self.sex = sex

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateChildCommand':
        data = Validator.validate_and_extract(CreateChildCommand.fields, args)

        birth_date = datetime.strptime(data["birth_date"], "%Y-%m-%d")
        if birth_date:
            data["birth_date"] = birth_date.isoformat()

        if "sex" in data:
            data['sex'] = data['sex'][0]

        return CreateChildCommand(**data)


class PatchChildCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),

        Field("name", "string", False),
        Field("birth_date", "integer", False, formatter=lambda x: int(x)),
        Field("sex", "string", False),
    ]

    def __init__(self, id: int, name: str = None, birth_date: int = None, sex: str = None):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.sex = sex

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchChildCommand':
        data = Validator.validate_and_extract(PatchChildCommand.fields, args)

        bd = data.get("birth_date", None)
        if bd:
            bd = datetime.fromtimestamp(data["birth_date"])
            data["birth_date"] = bd.strftime("%Y-%m-%d")

        return PatchChildCommand(**data)


class DeleteChildCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteChildCommand':
        data = Validator.validate_and_extract(DeleteChildCommand.fields, args)
        return DeleteChildCommand(**data)
