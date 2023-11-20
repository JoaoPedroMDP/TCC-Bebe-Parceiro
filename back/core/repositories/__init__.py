#  coding: utf-8
import logging
from abc import ABC, abstractmethod

from core.db_models.abstract_models import BaseModel
from core.utils.exceptions import NotFoundError


lgr = logging.getLogger(__name__)


class Repository(ABC):
    model: BaseModel = None

    @classmethod
    def create(cls, data: dict):
        obj = cls.model(**data)
        obj.save()
        return obj

    @classmethod
    def patch(cls, data: dict):
        obj = cls.get(data['id'])

        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
            else:
                lgr.warning(f"Tentativa de atribuição de atributo inexistente: {key} ({cls.model.readable_name})")

        obj.save()
        return obj

    @classmethod
    def filter(cls, **kwargs):
        return cls.model.objects.filter(**kwargs).order_by('id')

    @classmethod
    def get(cls, id: int):
        try:
            obj = cls.model.objects.get(id=id)
        except cls.model.DoesNotExist:
            raise NotFoundError(cls.model.readable_name)

        return obj

    @classmethod
    def delete(cls, id: int):
        obj = cls.get(id)
        obj.delete()
        return True
