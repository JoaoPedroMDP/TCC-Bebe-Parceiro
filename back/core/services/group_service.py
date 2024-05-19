#  coding: utf-8
from typing import List

from django.contrib.auth.models import Group

from core.repositories.group_repository import GroupRepository
from core.services import CrudService


class GroupService(CrudService):
    @classmethod
    def get_groups(cls) -> List[Group]:
        return GroupRepository.filter()
