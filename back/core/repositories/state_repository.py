#  coding: utf-8
import logging

from core.models import State
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class StateRepository(Repository):
    model = State
