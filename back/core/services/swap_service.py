#  coding: utf-8
from datetime import timedelta
import logging
from typing import List

from config import PENDING
from core.cqrs.commands.swap_commands import CreateSwapCommand, PatchSwapCommand, \
    DeleteSwapCommand
from core.cqrs.queries.swap_queries import GetSwapQuery, GetSwapsReportQuery, ListSwapQuery
from core.models import Beneficiary, Size, Swap
from core.repositories.child_repository import ChildRepository
from core.repositories.size_repository import SizeRepository
from core.repositories.status_repository import StatusRepository
from core.repositories.swap_repository import SwapRepository
from core.services import CrudService


lgr = logging.getLogger(__name__)


class SwapService(CrudService):
    @classmethod
    def create(cls, command: CreateSwapCommand) -> Swap:
        data = command.to_dict()
        data['cloth_size_id'] = SizeRepository.get(data['cloth_size_id']).id

        if 'shoe_size_id' in data:
            data['shoe_size_id'] = SizeRepository.get(data['shoe_size_id']).id
        
        data['child_id'] = ChildRepository.get(data['child_id']).id
        data['beneficiary_id'] = command.get_beneficiary_id()
        data['status_id'] = StatusRepository.get_by_name(PENDING).id
        return SwapRepository.create(data)

    @classmethod
    def patch(cls, command: PatchSwapCommand) -> Swap:
        return SwapRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListSwapQuery) -> List[Swap]:
        filters = query.to_dict()
        if query.user.is_beneficiary():
           lgr.debug("Usuária é beneficiária")
           filters = {
                **filters, 
                "beneficiary": query.user.beneficiary
            }

        if 'status_id' in filters:
            # Me certifico de que o status passado existe
            StatusRepository.get(filters['status_id'])
        
        return SwapRepository.filter(**filters)

    @classmethod
    def get(cls, query: GetSwapQuery) -> Swap:
        # TODO: Uma beneficiada só pode ver um troca se esta a pertencer
        return SwapRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteSwapCommand) -> bool:
        return SwapRepository.delete(command.id)

    @classmethod
    def get_reports(cls, query: GetSwapsReportQuery):
        filters = {}
        if query.start_date:
            filters['updated_at__gte'] = query.start_date
        
        if query.end_date:
            filters['updated_at__lte'] = query.end_date + timedelta(days=1)

        return SwapRepository.filter(**filters)