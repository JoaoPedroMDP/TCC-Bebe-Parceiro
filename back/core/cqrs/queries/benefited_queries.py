#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetBenefitedQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetBenefitedQuery':
        data = Validator.validate_and_extract(GetBenefitedQuery.fields, args)
        return GetBenefitedQuery(**data)


class ListBenefitedQuery(Query):
    fields = [
        Field("marital_status_id", "integer", False),
        Field("city_id", "integer", False),
        Field("birth_date", "integer", False),
        Field("child_count", "integer", False, formatter=lambda x: int(x)),
        Field("monthly_familiar_income", "float", False, formatter=lambda x: float(x)),
        Field("has_disablement", "boolean", False, formatter=lambda x: Validator.to_bool(x)),
        Field("social_programs", "list", False),
    ]

    def __init__(self, marital_status_id: int = None, city_id: int = None,
                 birth_date: str = None, child_count: int = None, monthly_familiar_income: float = None,
                 has_disablement: bool = None, social_programs: list = None):
        self.marital_status_id = marital_status_id
        self.city_id = city_id
        self.birth_date = birth_date
        self.child_count = child_count
        self.monthly_familiar_income = monthly_familiar_income
        self.has_disablement = has_disablement
        self.social_programs = social_programs

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListBenefitedQuery':
        data = Validator.validate_and_extract(ListBenefitedQuery.fields, args)
        return ListBenefitedQuery(**data)
