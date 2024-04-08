#  coding: utf-8
import logging
from abc import ABC
from typing import List

from rest_framework.views import APIView

from config import AUTH_ENABLED

lgr = logging.getLogger(__name__)


class BaseView(APIView, ABC):
    groups: List[str]

    permission_classes_by_method = {}
    authentication_classes_by_method = {}

    def get_permissions(self):
        if AUTH_ENABLED:
            try:
                return [permission() for permission in self.permission_classes_by_method[self.request.method.lower()]]
            except KeyError:
                # Retorna as permissões padrão caso não tenha sido definida nenhuma customizada para o método atual
                return [permission() for permission in self.permission_classes]
        else:
            return []

    def get_authenticators(self):
        if AUTH_ENABLED:
            try:
                return [authentication() for authentication in self.authentication_classes_by_method[self.request.method.lower()]]
            except KeyError:
                # Retorna as permissões padrão caso não tenha sido definida nenhuma customizada para o método atual
                return [authentication() for authentication in self.authentication_classes]
        else:
            return []
