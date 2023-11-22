#  coding: utf-8
from datetime import datetime

from core.cqrs import Query, Field, Validator


class GetChildQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetChildQuery':
        data = Validator.validate_and_extract(GetChildQuery.fields, args)
        return GetChildQuery(**data)


class ListChildQuery(Query):
    fields = [
        Field("birth_date", "integer", False, formatter=lambda x: int(x)),
        Field("benefited_id", "integer", False, formatter=lambda x: int(x)),
        Field("sex", "string", False),
    ]

    def __init__(self, birth_date: int = None, benefited_id: int = None, sex: str = None):
        self.birth_date = birth_date
        self.benefited_id = benefited_id
        self.sex = sex

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListChildQuery':
        data = Validator.validate_and_extract(ListChildQuery.fields, args)

        bd = data.get("birth_date", None)
        if bd:
            bd = datetime.fromtimestamp(data["birth_date"])
            data["birth_date"] = bd.strftime("%Y-%m-%d")

        return ListChildQuery(**data)
