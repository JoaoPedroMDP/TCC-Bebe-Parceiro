#  coding: utf-8
import logging

from core.models import AccessCode
from core.repositories import Repository
from core.utils.exceptions import NotFoundError


lgr = logging.getLogger(__name__)


class AccessCodeRepository(Repository):
    model = AccessCode
    pass
