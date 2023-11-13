#  coding: utf-8
import logging

from core.models import AccessCode
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class AccessCodeRepository(Repository):
    model = AccessCode
    pass
