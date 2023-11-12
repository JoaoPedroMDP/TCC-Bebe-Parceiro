#  coding: utf-8
import logging
from copy import copy
from typing import List, Dict, Callable, Union

from grappa import should
from django.http.request import QueryDict

from core.utils.dictable import Dictable
from core.utils.exceptions import ValidationErrors, WithHttpStatusCode


lgr = logging.getLogger(__name__)


class Field:
    def __init__(self, name: str, f_type: str, required: bool = False, default=None, formatter: Callable = None):
        self.name = name
        self.f_type = f_type
        self.required = required
        self.default = default
        self.formatter = formatter


class Validator:

    @staticmethod
    def to_bool(value: str) -> bool:
        if value.lower() in ['true', '1', 't', 'y', 'yes']:
            return True
        elif value.lower() in ['false', '0', 'f', 'n', 'no']:
            return False
        else:
            raise ValueError("Valor não é booleano")

    @staticmethod
    def validates(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AssertionError as e:
                raise WithHttpStatusCode(str(e), 400)

        return wrapper

    @staticmethod
    def has_field(data: Dict, field: Field) -> bool:
        return field.name in data

    @classmethod
    def validate_and_extract(cls, fields: List[Field], data: Union[Dict, QueryDict]) -> Dict:
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
                elif field.default is not None:
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
                errors.append("Campo '{}' deve ser do tipo '{}'".format(field.name, field.f_type))
                continue
            except ValueError as e:
                errors.append("Campo '{}' não é válido".format(field.name))
                continue

            # # Se for obrigatório e não existir, vapo
            # if field.required:
            #     if data.get(field.name) is None and field.default is None:
            #         errors.append("Campo '{}' é obrigatório".format(field.name))
            #         continue
            #     elif data.get(field.name) is None and field.default is not None:
            #         data[field.name] = field.default
            #
            # # Se existir, valida o tipo
            # if field.name in data:
            #     try:
            #         if field.formatter:
            #             data[field.name] = field.formatter(data[field.name])
            #
            #         data[field.name] | should.be.a(field.f_type)
            #         final_data[field.name] = data[field.name]
            #     except AssertionError as e:
            #         errors.append("Campo '{}' deve ser do tipo '{}'".format(field.name, field.f_type))
            #         continue
            #     except ValueError as e:
            #         errors.append("Campo '{}' não é válido".format(field.name))
            #         continue
            # else:
            #     lgr.warning("Campo '{}' não foi encontrado no dicionário".format(field.name))

        if len(errors) > 0:
            raise ValidationErrors(errors)

        return final_data


class Command(Validator, Dictable):
    pass


class Query(Validator, Dictable):
    pass
