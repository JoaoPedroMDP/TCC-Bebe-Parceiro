#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetProfessionalQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetProfessionalQuery':
        data = Validator.validate_and_extract(GetProfessionalQuery.fields, args)
        return GetProfessionalQuery(**data)


class ListProfessionalQuery(Query):
    fields = [
        Field("name", "string", False),
        Field("phone", "string", False),
        Field("speciality_id", "integer", False, formatter=lambda x: int(x)),
        Field("enabled", "bool", False, formatter=lambda x: Validator.to_bool(x)),
    ]

    def __init__(self, name: str = None, phone: str = None, speciality_id: int = None, enabled: bool = None):
        self.name = name
        self.phone = phone
        self.speciality_id = speciality_id
        self.enabled = enabled

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListProfessionalQuery':
        data = Validator.validate_and_extract(ListProfessionalQuery.fields, args)
        return ListProfessionalQuery(**data)

