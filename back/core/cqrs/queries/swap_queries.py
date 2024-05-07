#  coding: utf-8
from typing import Dict
from core.cqrs import Query, Field, Validator


class GetSwapQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetSwapQuery':
        data = Validator.validate_and_extract(GetSwapQuery.fields, args)
        return GetSwapQuery(**data)


class ListSwapQuery(Query):
    fields = [
        Field("cloth_size", "object", False),
        Field("shoe_size", "object", False),
        Field("description", "string", False),
        Field("child", "object", False),
    ]

    def __init__(self, cloth_size: dict = None, shoe_size: dict = None, description: str = None, child: dict = None):
        self.cloth_size = cloth_size
        self.shoe_size = shoe_size
        self.description = description
        self.child = child
        self.user = None

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListSwapQuery':
        data = Validator.validate_and_extract(ListSwapQuery.fields, args)
        return ListSwapQuery(**data)

    def to_dict(self) -> Dict:
        data = super().to_dict()
        del data['user']
        return data