#  coding: utf-8
import logging

from core.models import SocialProgram
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class SocialProgramRepository(Repository):
    model = SocialProgram
