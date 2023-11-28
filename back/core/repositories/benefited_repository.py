#  coding: utf-8
import logging

from core.models import Beneficiary
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class BenefitedRepository(Repository):
    model = Beneficiary
