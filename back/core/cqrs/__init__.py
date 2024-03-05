#  coding: utf-8
import logging
from copy import copy
from datetime import datetime
from typing import List, Dict, Callable, Union

from grappa import should
from django.http.request import QueryDict

from core.utils.dictable import Dictable
from core.utils.exceptions import ValidationErrors, HttpFriendlyError


lgr = logging.getLogger(__name__)


class Field:
    """
    Classe que representa um campo enviado em uma requisição.
    """
    def __init__(
            self, name: str, f_type: str, required: bool = False,
            default=None, formatter: Callable = None):
        self.name = name
        self.f_type = f_type
        self.required = required
        self.default = default
        # TODO: Definir se é melhor o Formatter ser usado antes ou depois de validar
        self.formatter = formatter


class Formatter:

    @staticmethod
    def to_bool(value: Union[str, bool, int]) -> bool:
        if value is True or value is False:
            return value
        elif value.lower() in ['true', 1, '1', 't', 'y', 'yes']:
            return True
        elif value.lower() in ['false', 0, '0', 'f', 'n', 'no']:
            return False
        else:
            raise ValueError("Valor não é booleano")

    @staticmethod
    def to_int(value: str) -> int:
        return int(value)

    @staticmethod
    def to_float(value: str) -> float:
        return float(value.replace(",", "."))

    @staticmethod
    def to_string(value: str) -> str:
        return value


class Validator(Formatter):
    """
    Classe que contém métodos utilitários para validação de dados.
    TODO: Posso adicionar funções que validam tipos mais específicos, como timestamp, essas coisas
    """

    @classmethod
    def date_not_on_future(cls, date: datetime):
        if date > datetime.now():
            raise AssertionError("Data de nascimento não pode ser no futuro")

    @staticmethod
    def validates(func):
        """
        Decorator que escuta por exceções do tipo "AssertionError" e as transforma em exceções retornáveis pela API.
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AssertionError as e:
                raise HttpFriendlyError(str(e), 400)

        return wrapper

    @staticmethod
    def has_field(data: Dict, field: Field) -> bool:
        """
        Verifica se o campo passado está no dicionário.
        """
        return field.name in data

    @classmethod
    def validate_and_extract(cls, fields: List[Field], data: Union[Dict, QueryDict]) -> Dict:
        """
        Valida os campos passados. Caso todos os campos sejam válidos, retorna um dicionário com os campos validados.
        Se um campo definir um formatter, o valor do campo será passado por ele antes de ser retornado.
        """
        if isinstance(data, QueryDict):
            data = copy(data)

        final_data = {}
        errors = []
        for field in fields:
            lgr.debug("Validando campo '{}'".format(field.name))
            default_used = False
            if not cls.has_field(data, field):
                lgr.debug("Campo '{}' não encontrado no dicionário".format(field.name))
                if field.required:
                    lgr.debug("Campo '{}' é obrigatório".format(field.name))
                    errors.append("Campo '{}' é obrigatório".format(field.name))
                    continue

                if field.default is not None:
                    lgr.debug("Campo '{}' não é obrigatório, mas possui valor default".format(field.name))
                    data[field.name] = field.default
                    default_used = True
                else:
                    lgr.debug("Campo '{}' não é obrigatório e não possui valor default".format(field.name))
                    continue

            if field.formatter and not default_used:
                lgr.debug("Campo '{}' possui formatter, aplicando".format(field.name))
                data[field.name] = field.formatter(data[field.name])
                lgr.debug("Campo '{}' após formatter: {}".format(field.name, data[field.name]))

            try:
                data[field.name] | should.be.a(field.f_type)
                final_data[field.name] = data[field.name]
            except AssertionError as e:
                errors.append("Campo '{}' deve ser do tipo '{}'. Recebido: {} ({})".format(
                    field.name,
                    field.f_type,
                    data[field.name],
                    type(data[field.name])
                ))
                continue
            except ValueError as e:
                errors.append("Campo '{}' não é válido".format(field.name))
                continue

        if len(errors) > 0:
            raise ValidationErrors(errors)

        return final_data


# TODO: Criar uma função to_db que retorna apenas os campos daquele model no banco de dados
# A ideia é que eu não precise montar na mão o dicionário com os dados, filtrando informações paralelas do front
# Exemplo: Na rota POST de beneficiada, eu recebo o Access Code, e ele fica no command. Mas na hora de criar uma nova
# beneficiada, eu não passo o Access Code pois ele não faz parte da tabela do banco de dados dela
class Command(Validator, Dictable):
    pass


class Query(Validator, Dictable):
    pass
