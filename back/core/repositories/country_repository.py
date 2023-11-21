#  coding: utf-8
import logging

from core.models import Country
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class CountryRepository(Repository):
    model = Country
