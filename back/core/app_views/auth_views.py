#  coding: utf-8
import logging
from typing import List

from django.contrib.auth import login
from django.contrib.auth.models import Group
from rest_framework.request import Request

from core.app_views import BaseView
from core.permissions.at_least_one_group import AtLeastOneGroup
from core.serializers import GroupSerializer
from core.services.group_service import GroupService
from config import MANAGE_VOLUNTEERS
from core.models import Beneficiary, User, Volunteer
from core.repositories.beneficiary_repository import BeneficiaryRepository
from core.repositories.volunteer_repository import VolunteerRepository
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer

from core.utils.decorators import endpoint

lgr = logging.getLogger(__name__)


# Copiei de https://jazzband.github.io/django-rest-knox/auth/
class LoginView(KnoxLoginView):
    authentication_classes = ()
    permission_classes = ()

    @endpoint
    def post(self, request, format=None):
        # Request.data precisa ter username e password, lembre-se disso
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = serializer.validated_data['user']
        login(request, user)
        response = super(LoginView, self).post(request, format=None)


        if user.is_volunteer():
            person: Volunteer = VolunteerRepository.filter(user=user)[0]
        else :
            person: Beneficiary = BeneficiaryRepository.filter(user=user)[0]

        response.data['person_id'] = person.id
        return response.data, response.status_code


class GroupGenericView(BaseView):
    groups = [MANAGE_VOLUNTEERS]
    permission_classes = (AtLeastOneGroup,)

    @endpoint
    def get(self, request: Request, format=None):
        groups: List[Group] = GroupService.get_groups()
        return GroupSerializer(groups, many=True).data, 200
