import logging
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.app_views import BaseView


lgr = logging.getLogger(__name__)

class IsBeneficiary(BasePermission):

    def has_permission(self, request: Request, view: BaseView):
        has = request.user.is_beneficiary()
        has or lgr.warning("Usuário não é beneficiário")
        return has