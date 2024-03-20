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
        Field("name", "string", True),
        Field("email", "string", True),
        Field("phone", "string", True),
        Field("speciality_id", "integer", True, formatter=lambda x: int(x)),
        Field("city_id", "integer", False, formatter=lambda x: int(x)),
    ]

    def __init__(self, name: str, email: str, phone: str, speciality_id: int, city_id: int):
        self.name = name
        self.email = email
        self.phone = phone
        self.speciality_id = speciality_id
        self.city_id = city_id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListProfessionalQuery':
        data = Validator.validate_and_extract(ListProfessionalQuery.fields, args)
        return ListProfessionalQuery(**data)
