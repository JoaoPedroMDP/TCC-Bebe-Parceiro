#  coding: utf-8
import logging

from core.models import User
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class UserRepository(Repository):
    model = User
