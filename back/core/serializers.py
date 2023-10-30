#  coding: utf-8
from rest_framework.serializers import ModelSerializer

from core.models import AccessCode


class AccessCodeSerializer(ModelSerializer):
    class Meta:
        model = AccessCode
        fields = ['id', 'code', 'used']
