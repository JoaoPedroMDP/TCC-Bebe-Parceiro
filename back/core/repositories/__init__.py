#  coding: utf-8
import json
import logging
from abc import ABC

from core.models import BaseModel
from core.utils.exceptions import NotFoundError


lgr = logging.getLogger(__name__)


class Repository(ABC):
    model: BaseModel = None

    @classmethod
    def fill(cls, data: dict, model: BaseModel):
        for key, value in data.items():
            if hasattr(model, key):
                lgr.debug(f"Atribuindo {value} para coluna {key}")
                setattr(model, key, value)
            else:
                lgr.warning(f"Tentativa de atribuição em coluna inexistente: {key} ({cls.model.readable_name})")

        return model

    @classmethod
    def create(cls, data: dict):
        obj = cls.fill(data, cls.model())
        obj.save()
        return obj

    @classmethod
    def patch(cls, data: dict):
        obj = cls.get(data['id'])
        obj = cls.fill(data, obj)
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
