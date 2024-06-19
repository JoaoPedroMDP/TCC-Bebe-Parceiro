#  coding: utf-8
import logging

from core.models import Size
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class SizeRepository(Repository):
    model = Size
