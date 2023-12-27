#  coding: utf-8
import logging

from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions

lgr = logging.getLogger(__name__)


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
