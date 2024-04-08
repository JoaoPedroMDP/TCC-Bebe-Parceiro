#  coding: utf-8
import logging
from datetime import datetime
from typing import Dict

from config import MANAGE_BENEFICIARIES
from core.cqrs import Validator, Field, Command
from core.models import User

lgr = logging.getLogger(__name__)


class CreateBeneficiaryCommand(Command):
    fields = [
        Field("access_code", "string", False),
        Field("name", "string", True),
        Field("phone", "string", True),
        Field("password", "string", True),
        Field("children", "list", True),
        Field("marital_status_id", "integer", True, formatter=lambda x: int(x)),
        Field("city_id", "integer", True, formatter=lambda x: int(x)),
        Field("birth_date", "string", True),
        Field("child_count", "integer", True, formatter=lambda x: int(x)),
        Field("monthly_familiar_income", "float", True, formatter=lambda x: float(x)),
        Field("has_disablement", "boolean", True, formatter=lambda x: Validator.to_bool(x)),

        Field("email", "string", False),
        Field("social_programs", "list", False),
        Field("user", "object", False)
    ]

    def __init__(self,
                 marital_status_id: int, city_id: int, birth_date: str, child_count: int,
                 monthly_familiar_income: float, has_disablement: bool, social_programs: list = None,
                 access_code: str = None, name: str = None, phone: str = None, password: str = None,
                 children: list = None, email: str = None, user: User = None):
        self.marital_status_id = marital_status_id
        self.city_id = city_id
        self.birth_date = birth_date
        self.child_count = child_count
        self.monthly_familiar_income = monthly_familiar_income
        self.has_disablement = has_disablement
        self.social_programs = social_programs
        self.access_code = access_code
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.children = children
        self.user = user

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateBeneficiaryCommand':
        data: Dict = Validator.validate_and_extract(CreateBeneficiaryCommand.fields, args)

        # Valido a data de nascimento
        birth_date = datetime.strptime(data["birth_date"], "%Y-%m-%d")
        Validator.date_not_on_future(birth_date)
        data["birth_date"] = birth_date.isoformat()

        # Valido a quantidade de filhos
        if data["child_count"] < 0:
            raise AssertionError("Quantidade de filhos não pode ser negativa")

        # Valido a permissão do usuário. Caso seja uma voluntária que está criando uma beneficiada, não é necessário
        # passar o código de acesso
        if "access_code" not in data and not data["user"].groups.filter(name=MANAGE_BENEFICIARIES).exists():
            raise AssertionError("Usuário não tem permissão para criar beneficiadas sem código de acesso")

        return CreateBeneficiaryCommand(**data)


class PatchBeneficiaryCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),

        Field("name", "string", False),
        Field("phone", "string", False),
        Field("password", "string", False),
        Field("children", "list", False),
        Field("marital_status_id", "integer", False, formatter=lambda x: int(x)),
        Field("city_id", "integer", False, formatter=lambda x: int(x)),
        Field("birth_date", "integer", False, formatter=lambda x: int(x)),
        Field("child_count", "integer", False, formatter=lambda x: int(x)),
        Field("monthly_familiar_income", "float", False, formatter=lambda x: float(x)),
        Field("has_disablement", "boolean", False, formatter=lambda x: Validator.to_bool(x)),
        Field("social_programs", "list", False),
    ]

    def __init__(self, id: int, marital_status_id: int = None, city_id: int = None,
                 birth_date: str = None, child_count: int = None, monthly_familiar_income: float = None,
                 has_disablement: bool = None, social_programs: list = None):
        self.id = id
        self.marital_status_id = marital_status_id
        self.city_id = city_id
        self.birth_date = birth_date
        self.child_count = child_count
        self.monthly_familiar_income = monthly_familiar_income
        self.has_disablement = has_disablement
        self.social_programs = social_programs

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchBeneficiaryCommand':
        data = Validator.validate_and_extract(PatchBeneficiaryCommand.fields, args)

        # Valido a data de nascimento
        birth_date = datetime.strptime(data["birth_date"], "%Y-%m-%d")
        Validator.date_not_on_future(birth_date)
        data["birth_date"] = birth_date.isoformat()

        return PatchBeneficiaryCommand(**data)


class DeleteBeneficiaryCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteBeneficiaryCommand':
        data = Validator.validate_and_extract(DeleteBeneficiaryCommand.fields, args)
        return DeleteBeneficiaryCommand(**data)
