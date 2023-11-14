#  coding: utf-8
import logging

from core.models import Benefited
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class BenefitedRepository(Repository):
    model = Benefited
