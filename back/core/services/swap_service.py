#  coding: utf-8
import logging
from typing import List

from config import PENDING
from core.cqrs.commands.swap_commands import CreateSwapCommand, PatchSwapCommand, \
    DeleteSwapCommand
from core.cqrs.queries.swap_queries import GetSwapQuery, ListSwapQuery
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
        lgr.debug(data)
        return SwapRepository.create(data)

    @classmethod
    def patch(cls, command: PatchSwapCommand) -> Swap:
        return SwapRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListSwapQuery) -> List[Swap]:
        filters = query.to_dict()
        
        try:
           query.user.beneficiary
           lgr.debug("Usuária é beneficiária")
           filters = {
                **filters, 
                "beneficiary": query.user.beneficiary
            }
        except Beneficiary.DoesNotExist as e:
            lgr.debug("Usuária é voluntária")
            # Significa que é uma voluntária
            pass

        if 'status' in filters:
            status = StatusRepository.get_by_name(filters['status'])
            filters['status_id'] = status.id
            del filters['status']

        return SwapRepository.filter(**filters)

    @classmethod
    def get(cls, query: GetSwapQuery) -> Swap:
        return SwapRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteSwapCommand) -> bool:
        return SwapRepository.delete(command.id)
