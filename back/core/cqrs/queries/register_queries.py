#  coding: utf-8

from core.cqrs import Field, Query, Validator


class GetRegisterQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetRegisterQuery':
        data = Validator.validate_and_extract(GetRegisterQuery.fields, args)
        return GetRegisterQuery(**data)


class ListRegisterQuery(Query):
    fields = [
        Field("beneficiary_id", "integer", False, formatter=lambda x: int(x)),
    ]

    def __init__(self, beneficiary_id: int = None):
        self.beneficiary_id = beneficiary_id
    
    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListRegisterQuery':
        data = Validator.validate_and_extract(ListRegisterQuery.fields, args)
        return ListRegisterQuery(**data)
