#  coding: utf-8
import logging

from django.contrib.auth.models import Group

from core.repositories import Repository

lgr = logging.getLogger(__name__)


class GroupRepository(Repository):
    model = Group
