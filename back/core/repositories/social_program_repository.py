#  coding: utf-8
import logging

from core.models import SocialProgram
from core.repositories import Repository
from core.utils.exceptions import NotFoundError


lgr = logging.getLogger(__name__)


class SocialProgramRepository(Repository):
    model = SocialProgram

    @classmethod
    def list(cls, filters: dict):
        return super().list(**filters)
