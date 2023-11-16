#  coding: utf-8
import logging

from core.db_models.adress_related_models import State
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class StateRepository(Repository):
    model = State
