#  coding: utf-8
import logging

from core.models import Speciality
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class SpecialityRepository(Repository):
    model = Speciality
