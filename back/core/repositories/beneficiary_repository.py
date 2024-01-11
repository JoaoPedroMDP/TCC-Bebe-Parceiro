#  coding: utf-8
import logging

from core.models import Beneficiary
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class BeneficiaryRepository(Repository):
    model = Beneficiary
