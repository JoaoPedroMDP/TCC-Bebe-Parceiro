#  coding: utf-8
from datetime import datetime
import logging

from django.http import QueryDict

from core.cqrs import Query, Field, Validator


lgr = logging.getLogger(__name__)


class GetVolunteerQuery(Query):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetVolunteerQuery':
        data = Validator.validate_and_extract(GetVolunteerQuery.fields, args)
        return GetVolunteerQuery(**data)


class ListVolunteerQuery(Query):
    fields = [
        Field("group_ids", "list", False),
        Field("city_id", "integer", False, formatter=lambda x: int(x)),
    ]

    def __init__(self, group_ids: list = None, city_id: int = None):
        self.group_ids = group_ids
        self.city_id = city_id

    @staticmethod
    @Validator.validates
    def from_dict(args: QueryDict) -> 'ListVolunteerQuery':
        raw_data = args.dict()
        if 'group_ids' in raw_data:
            raw_data['group_ids'] = args.getlist('group_ids')

        data = Validator.validate_and_extract(ListVolunteerQuery.fields, raw_data)
        return ListVolunteerQuery(**data)

class GetVolunteersReportQuery(Query):
    fields = [
        Field("start_date", "string", False),
        Field("end_date", "string", False),
    ]

    def __init__(self, start_date: str = None, end_date: str = None):
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'GetVolunteersReportQuery':
        data = Validator.validate_and_extract(GetVolunteersReportQuery.fields, args)

        if data['start_date']:
            data['start_date'] = datetime.fromisoformat(data['start_date'])

        if data['end_date']:
            data['end_date'] = datetime.fromisoformat(data['end_date'])

        return GetVolunteersReportQuery(**data)
    