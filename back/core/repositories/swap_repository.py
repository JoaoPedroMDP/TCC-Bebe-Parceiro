#  coding: utf-8
import logging

from core.models import Swap
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class SwapRepository(Repository):
    model = Swap
