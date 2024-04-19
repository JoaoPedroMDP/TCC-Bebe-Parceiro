#  coding: utf-8
import logging

from django.contrib.auth import login
from core.utils.exceptions import HttpFriendlyError
from config import ROLE_ADMIN, ROLE_BENEFICIARY, ROLE_PENDING_BENEFICIARY, ROLE_VOLUNTEER
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


    # Request.data precisa ter username e password, lembre-se disso
    @endpoint
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = serializer.validated_data['user']
        login(request, user)
        response = super(LoginView, self).post(request, format=None)
        role: str = user.role

        if role in [ROLE_ADMIN, ROLE_VOLUNTEER]:
            person: Volunteer = VolunteerRepository.filter(user=user)[0]
        elif role in [ROLE_BENEFICIARY, ROLE_PENDING_BENEFICIARY]:
            person: Beneficiary = BeneficiaryRepository.filter(user=user)[0]
        else:
            raise HttpFriendlyError("Role inválida", status_code=500)

        response.data['person_id'] = person.id
        return response.data, response.status_code
