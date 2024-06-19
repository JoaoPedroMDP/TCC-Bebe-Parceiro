#  coding: utf-8
import logging

from core.models import Register
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class RegisterRepository(Repository):
    model = Register
