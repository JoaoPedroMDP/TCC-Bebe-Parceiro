from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.app_views import BaseView

class OwnsIt(BasePermission):

    def has_permission(self, request: Request, view: BaseView):
        pass
