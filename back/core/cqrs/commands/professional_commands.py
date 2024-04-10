#  coding: utf-8
from core.cqrs import Validator, Field, Command


class CreateProfessionalCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("phone", "string", True),
        Field("speciality_id", "integer", True, formatter=lambda x: int(x)),
        Field("accepted_volunteer_terms", "boolean", True, formatter=lambda x: Validator.to_bool(x)),
    ]

    def __init__(self, name: str, email: str, phone: str, speciality_id: int,
                 accepted_volunteer_terms: bool):
        self.name = name
        self.phone = phone
        self.speciality_id = speciality_id
        self.accepted_volunteer_terms = accepted_volunteer_terms


    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateProfessionalCommand':
        data = Validator.validate_and_extract(CreateProfessionalCommand.fields, args)
        return CreateProfessionalCommand(**data)


class PatchProfessionalCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
        Field("phone", "string", False),
        Field("speciality_id", "integer", False, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int, name: str = None, phone: str = None, speciality_id: int = None):
        self.id = id
        self.name = name
        self.phone = phone
        self.speciality_id = speciality_id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchProfessionalCommand':
        data = Validator.validate_and_extract(PatchProfessionalCommand.fields, args)
        return PatchProfessionalCommand(**data)


class DeleteProfessionalCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteProfessionalCommand':
        data = Validator.validate_and_extract(DeleteProfessionalCommand.fields, args)
        return DeleteProfessionalCommand(**data)
