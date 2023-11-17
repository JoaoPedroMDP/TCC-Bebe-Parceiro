#  coding: utf-8
from core.cqrs import Validator, Field, Command


class CreateBenefitedCommand(Command):
    fields = [
        Field("marital_status_id", "integer", True),
        Field("city_id", "integer", True, formatter=lambda x: int(x)),
        Field("birth_date", "integer", True, formatter=lambda x: int(x)),
        Field("child_count", "integer", True, formatter=lambda x: int(x)),
        Field("monthly_familiar_income", "float", True, formatter=lambda x: float(x)),
        Field("has_disablement", "boolean", True, formatter=lambda x: Validator.to_bool(x)),
        Field("social_programs", "list", False),
    ]

    def __init__(self, marital_status_id: int, city_id: int, birth_date: str,
                 child_count: int, monthly_familiar_income: float, has_disablement: bool, social_programs: list = None):
        self.marital_status_id = marital_status_id
        self.city_id = city_id
        self.birth_date = birth_date
        self.child_count = child_count
        self.monthly_familiar_income = monthly_familiar_income
        self.has_disablement = has_disablement
        self.social_programs = social_programs

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateBenefitedCommand':
        data = Validator.validate_and_extract(CreateBenefitedCommand.fields, args)
        return CreateBenefitedCommand(**data)


class PatchBenefitedCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),

        Field("marital_status_id", "integer", False, formatter=lambda x: int(x)),
        Field("city_id", "integer", False, formatter=lambda x: int(x)),
        Field("birth_date", "integer", False, formatter=lambda x: int(x)),
        Field("child_count", "integer", False, formatter=lambda x: int(x)),
        Field("monthly_familiar_income", "float", False, formatter=lambda x: float(x)),
        Field("has_disablement", "boolean", False, formatter=lambda x: Validator.to_bool(x)),
        Field("social_programs", "list", False),
    ]

    def __init__(self, id: int, marital_status_id: int = None, city_id: int = None,
                 birth_date: str = None, child_count: int = None, monthly_familiar_income: float = None,
                 has_disablement: bool = None, social_programs: list = None):
        self.id = id
        self.marital_status_id = marital_status_id
        self.city_id = city_id
        self.birth_date = birth_date
        self.child_count = child_count
        self.monthly_familiar_income = monthly_familiar_income
        self.has_disablement = has_disablement
        self.social_programs = social_programs

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchBenefitedCommand':
        data = Validator.validate_and_extract(PatchBenefitedCommand.fields, args)
        return PatchBenefitedCommand(**data)


class DeleteBenefitedCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteBenefitedCommand':
        data = Validator.validate_and_extract(DeleteBenefitedCommand.fields, args)
        return DeleteBenefitedCommand(**data)
