#  coding: utf-8
from core.cqrs import Validator, Field, Command

class CreateRegisterCommand(Command):
    fields = [
        Field("appointment_id", "integer", True, formatter=lambda x: int(x)),
        Field("volunteer_id", "integer", True, formatter=lambda x: int(x)),
        Field("beneficiary_id", "integer", True, formatter=lambda x: int(x)),
        Field("description", "string", True)
    ]

    def __init__(self, appointment_id: int, volunteer_id: int, description: str, beneficiary_id: int):
        self.appointment_id = appointment_id
        self.volunteer_id = volunteer_id
        self.beneficiary_id = beneficiary_id
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
