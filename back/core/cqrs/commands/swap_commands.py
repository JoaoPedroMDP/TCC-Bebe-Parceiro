#  coding: utf-8
import logging
from typing import Dict
from config import PENDING
from core.cqrs import Validator, Field, Command
from core.models import Beneficiary, Child, User
from core.repositories.beneficiary_repository import BeneficiaryRepository

lgr = logging.getLogger(__name__)

def ben_owns_child(ben: Beneficiary, child_id: int):
    try:
        ben.children.get(id=child_id)
    except Child.DoesNotExist:
        raise AssertionError("A criança não pertence à beneficiária")


def no_pending_swap(ben: Beneficiary):
    if ben.has_pending_swap():
        raise AssertionError("Beneficiária já possui uma troca pendente")


def get_ben(data: dict, args: dict):
    if args['user'].is_beneficiary():
        ben = args['user'].beneficiary
    else:
        ben = BeneficiaryRepository.get(data['beneficiary_id'])
    
    return ben


def vol_specified_ben(data: dict, args: dict):
    if not args['user'].is_beneficiary() and 'beneficiary_id' not in data:
        raise AssertionError("Beneficiária não especificada")


class CreateSwapCommand(Command):
    fields = [
        Field("cloth_size_id", "integer", True, formatter=lambda x: int(x)),
        Field("child_id", "integer", True, formatter=lambda x: int(x)),
        Field("beneficiary_id", "integer", False, formatter=lambda x: int(x)),
        Field("shoe_size_id", "integer", False, formatter=lambda x: int(x)),
        Field("description", "string", False),
    ]

    def __init__(
            self, cloth_size_id: dict, shoe_size_id: dict = None, 
            description: str = None, child_id: dict = None, beneficiary_id: int = None,
            user: User = None):
        self.cloth_size_id: int = cloth_size_id
        self.shoe_size_id: int = shoe_size_id
        self.description: str = description
        self.child_id: int = child_id
        self.beneficiary_id: int = beneficiary_id
        self.user: User = user

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateSwapCommand':
        data = Validator.validate_and_extract(CreateSwapCommand.fields, args)

        # Caso seja uma voluntária criando a troca, precisa especificar o campo beneficiary_id
        vol_specified_ben(data, args)
        # Pego a beneficiária pois preciso validar algumas coisas
        ben = get_ben(data, args)
        # Uma beneficiada não pode ter duas trocas ativas
        no_pending_swap(ben)
        # Valido se a criança é dela mesmo
        ben_owns_child(ben, data['child_id'])

        return CreateSwapCommand(**data, user=args['user'])

    def get_beneficiary_id(self):
        if self.user.is_beneficiary():
            return self.user.beneficiary.id

        return self.beneficiary_id

    def to_dict(self) -> Dict:
        data = super().to_dict()
        del data['user']
        return data


class PatchSwapCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("cloth_size_id", "integer", False, formatter=lambda x: int(x)),
        Field("child_id", "integer", False, formatter=lambda x: int(x)),
        Field("beneficiary_id", "integer", False, formatter=lambda x: int(x)),
        Field("shoe_size_id", "integer", False, formatter=lambda x: int(x)),
        Field("description", "string", False),
        Field("status_id", "integer", False, formatter=lambda x: int(x))
    ]

    def __init__(
            self, id: int, cloth_size_id: int = None, shoe_size_id: int = None,
            description: str = None, child_id: int = None, beneficiary_id: int = None,
            status_id: int = None):
        self.id = id
        self.cloth_size_id = cloth_size_id
        self.shoe_size_id = shoe_size_id
        self.description = description
        self.child_id = child_id
        self.beneficiary_id = beneficiary_id
        self.status_id = status_id
    
    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchSwapCommand':
        data = Validator.validate_and_extract(PatchSwapCommand.fields, args)
        return PatchSwapCommand(**data)


class DeleteSwapCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteSwapCommand':
        data = Validator.validate_and_extract(DeleteSwapCommand.fields, args)
        return DeleteSwapCommand(**data)
