#  coding: utf-8
from core.cqrs import Query, Field, Validator


class GetCampaignQuery(Query):
    fields = [
        Field("id", "integer", False, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetCampaignQuery':
        data = Validator.validate_and_extract(GetCampaignQuery.fields, args)
        return GetCampaignQuery(**data)


class ListCampaignQuery(Query):
    fields = [
        Field("name", "string", False),
        Field("start_date", "string", False),
        Field("end_date", "string", False),
        Field("description", "string", False),
        Field("external_link", "string", False),
    ]

    def __init__(self, name: str = None, start_date: str = None, end_date: str = None,
                 description: str = None, external_link: str = None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.external_link = external_link

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'ListCampaignQuery':
        data = Validator.validate_and_extract(ListCampaignQuery.fields, args)
        return ListCampaignQuery(**data)
