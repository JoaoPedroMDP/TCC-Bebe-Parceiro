#  coding: utf-8
import logging

from core.models import Campaign
from core.repositories import Repository

lgr = logging.getLogger(__name__)


class CampaignRepository(Repository):
    model = Campaign
