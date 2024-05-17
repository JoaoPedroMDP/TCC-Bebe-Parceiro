#  coding: utf-8
import logging

from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.app_views import BaseView

lgr = logging.getLogger(__name__)


class AtLeastOneGroup(BasePermission):
    """
    Permite acesso a uma view se o usuário pertencer a pelo menos um dos grupos especificados
    """
    def has_permission(self, request: Request, view: BaseView):
        lgr.debug(request.user.groups.all())
        groups = list(request.user.groups.all())
        for g in groups:
            if g.name in view.groups:
                return True

        lgr.warning("Usuário não pertence a nenhum dos grupos permitidos")
        return False
