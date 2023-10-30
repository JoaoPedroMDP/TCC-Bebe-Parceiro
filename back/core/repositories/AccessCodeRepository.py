#  coding: utf-8
import logging

from core.models import AccessCode
from core.utils.exceptions import NotFoundError


lgr = logging.getLogger(__name__)


class AccessCodeRepository:

    @classmethod
    def get(cls, id: int):
        access_code = AccessCode.objects.get(id=id)
        if access_code:
            return access_code

        raise NotFoundError("Código de acesso")

    @classmethod
    def patch(cls, data: dict):
        access_code: AccessCode = cls.get(data['id'])
        for key, value in data.items():
            if hasattr(access_code, key):
                setattr(access_code, key, value)
            else:
                lgr.warning("Tentativa de atribuição de atributo inexistente: {} (AccessCode)".format(key))

        access_code.save()
        return access_code

    @classmethod
    def delete(cls, id: int):
        access_code: AccessCode = cls.get(id)
        access_code.delete()
        return True
