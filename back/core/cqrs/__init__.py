#  coding: utf-8
from typing import List, Dict, Callable

from grappa import should

from core.utils.dictable import Dictable
from core.utils.exceptions import ValidationErrors, WithHttpStatusCode


class Field:
    def __init__(self, name: str, f_type: str, required: bool = False, default=None, formatter: Callable = None):
        self.name = name
        self.f_type = f_type
        self.required = required
        self.default = default
        self.formatter = formatter


class Validator:

    @staticmethod
    def validates(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AssertionError as e:
                raise WithHttpStatusCode(str(e), 400)

        return wrapper

    @classmethod
    def validate_and_extract(cls, fields: List[Field], original_data: Dict) -> Dict:
        # Eu copio pq o Django me entrega um QueryDict, que é imutável, e se tiver um formatador vai ter que alterar
        copied_data = {k: v for k, v in original_data.items()}
        final_data = {}
        errors = []
        for field in fields:
            # Se for obrigatório e não existir, vapo
            if field.required and copied_data.get(field.name) is None:
                errors.append("Campo '{}' é obrigatório".format(field.name))
                continue

            # Se existir, valida o tipo
            if field.name in copied_data:
                try:
                    if field.formatter:
                        copied_data[field.name] = field.formatter(copied_data[field.name])

                    copied_data[field.name] | should.be.a(field.f_type)
                    final_data[field.name] = copied_data[field.name]
                except AssertionError as e:
                    errors.append("Campo '{}' deve ser do tipo '{}'".format(field.name, field.f_type))
                    continue
                except ValueError as e:
                    errors.append("Campo '{}' não é válido".format(field.name))
                    continue
            elif field.default is not None:
                copied_data[field.name] = field.default

        if len(errors) > 0:
            raise ValidationErrors(errors)

        return final_data


class Command(Validator, Dictable):
    pass


class Query(Validator, Dictable):
    pass
