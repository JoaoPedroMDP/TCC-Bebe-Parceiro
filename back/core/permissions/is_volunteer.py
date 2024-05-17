import logging
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.app_views import BaseView


lgr = logging.getLogger(__name__)

class IsVolunteer(BasePermission):

    def has_permission(self, request: Request, view: BaseView):
        has = request.user.is_volunteer()
        has or lgr.warning("Usuário não é voluntário")
        return has