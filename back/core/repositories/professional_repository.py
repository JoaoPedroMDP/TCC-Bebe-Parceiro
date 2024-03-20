#  coding: utf-8
import logging

from core.models import Professional
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class ProfessionalRepository(Repository):
    model = Professional
