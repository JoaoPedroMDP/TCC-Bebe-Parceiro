#  coding: utf-8
import logging
from typing import Dict

from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.app_views import BaseView
from core.models import Beneficiary, Volunteer, TimestampedModel

lgr = logging.getLogger(__name__)

class IsIt(BasePermission):
    URIS_MODELS: Dict[str, TimestampedModel] = {
        "beneficiaries": Beneficiary,
        "voluntaries": Volunteer
    }

    def has_permission(self, request: Request, view: BaseView):
        uri, obj_id = request.get_full_path().split("/")[1:]
        model: TimestampedModel = self.URIS_MODELS.get(uri)

        item = model.objects.filter(id=int(obj_id), user=request.user).first()
        has = item is not None 
        has or lgr.warning("Usuário não é dono do objeto")
        return has
