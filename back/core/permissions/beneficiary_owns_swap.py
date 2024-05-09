import logging
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.app_views import BaseView


lgr = logging.getLogger(__name__)


class BeneficiaryOwnsSwap(BasePermission):

    def has_permission(self, request: Request, view: BaseView):
        if request.user.is_beneficiary():
            return request.user.beneficiary.swaps.filter(id=view.kwargs['pk']).exists()

