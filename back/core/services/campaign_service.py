#  coding: utf-8
from typing import List

from core.cqrs.commands.campaign_commands import CreateCampaignCommand, PatchCampaignCommand, \
    DeleteCampaignCommand
from core.cqrs.queries.campaign_queries import GetCampaignQuery, ListCampaignQuery
from core.models import Campaign
from core.repositories.campaign_repository import CampaignRepository
from core.services import CrudService


class CampaignService(CrudService):
    @classmethod
    def create(cls, command: CreateCampaignCommand) -> Campaign:
        new_campaign = CampaignRepository.create(command.to_dict())
        return new_campaign

    @classmethod
    def patch(cls, command: PatchCampaignCommand) -> Campaign:
        return CampaignRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListCampaignQuery) -> List[Campaign]:
        return CampaignRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetCampaignQuery) -> Campaign:
        return CampaignRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteCampaignCommand) -> bool:
        return CampaignRepository.delete(command.id)
