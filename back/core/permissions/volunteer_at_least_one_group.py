#  coding: utf-8
import logging

from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.app_views import BaseView

lgr = logging.getLogger(__name__)


class VolunteerAtLeastOneGroup(BasePermission):
    """
    Permite acesso a uma view se o usuário for uma voluntária e pertencer a pelo menos um dos grupos especificados
    """
    def has_permission(self, request: Request, view: BaseView):
        groups = list(request.user.groups.all())
        if request.user.role == 'volunteer':
            for g in groups:
                if g.name in view.groups:
                    return True

        return False
