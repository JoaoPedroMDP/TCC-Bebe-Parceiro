#  coding: utf-8
from rest_framework.serializers import ModelSerializer

from core.models import AccessCode, SocialProgram


class AccessCodeSerializer(ModelSerializer):
    class Meta:
        model = AccessCode
        fields = ['id', 'code', 'used']


class SocialProgramSerializer(ModelSerializer):
    class Meta:
        model = SocialProgram
        fields = ['id', 'name', 'enabled']
