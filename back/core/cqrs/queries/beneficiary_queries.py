#  coding: utf-8
from datetime import datetime
from core.cqrs import Query, Field, Validator


class GetBeneficiaryQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetBeneficiaryQuery':
        data = Validator.validate_and_extract(GetBeneficiaryQuery.fields, args)
        return GetBeneficiaryQuery(**data)


class ListBeneficiaryQuery(Query):
    fields = [
        Field("user_id", "integer", False, formatter=lambda x: int(x)),
        Field("marital_status_id", "integer", False, formatter=lambda x: int(x)),
        Field("city_id", "integer", False, formatter=lambda x: int(x)),
        Field("birth_date", "integer", False, formatter=lambda x: int(x)),
        Field("child_count", "integer", False, formatter=lambda x: int(x)),
        Field("monthly_familiar_income", "float", False, formatter=lambda x: float(x)),
        Field("has_disablement", "boolean", False, formatter=lambda x: Validator.to_bool(x)),
        Field("social_programs", "list", False),
        Field("approved", "boolean", False),
    ]

    def __init__(self, user_id: int = None, marital_status_id: int = None, city_id: int = None,
                 birth_date: str = None, child_count: int = None, monthly_familiar_income: float = None,
                 has_disablement: bool = None, social_programs: list = None, approved: bool = None):
        self.user_id = user_id
        self.marital_status_id = marital_status_id
        self.city_id = city_id
        self.birth_date = birth_date
        self.child_count = child_count
        self.monthly_familiar_income = monthly_familiar_income
        self.has_disablement = has_disablement
        self.social_programs = social_programs
        self.approved = approved

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListBeneficiaryQuery':
        data = Validator.validate_and_extract(ListBeneficiaryQuery.fields, args)
        return ListBeneficiaryQuery(**data)


class GetBeneficiariesReportQuery(Query):
    fields = [
        Field("start_date", "string", False),
        Field("end_date", "string", False),
    ]

    def __init__(self, start_date: str = None, end_date: str = None):
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetBeneficiariesReportQuery':
        data = Validator.validate_and_extract(GetBeneficiariesReportQuery.fields, args)

        if 'start_date' in data:
            data['start_date'] = datetime.fromisoformat(data['start_date'])

        if 'end_date' in data:
            data['end_date'] = datetime.fromisoformat(data['end_date'])

        return GetBeneficiariesReportQuery(**data)
    