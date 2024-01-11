#  coding: utf-8
import logging

from core.models import Volunteer
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class VolunteerRepository(Repository):
    model = Volunteer
