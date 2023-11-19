#  coding: utf-8
from rest_framework.serializers import ModelSerializer

from core.db_models.adress_related_models import Country, State, City
from core.models import AccessCode, SocialProgram, MaritalStatus, Benefited


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class StateSerializer(ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = State
        fields = ['id', 'name', 'country']


class CitySerializer(ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'state']


class AccessCodeSerializer(ModelSerializer):
    class Meta:
        model = AccessCode
        fields = ['id', 'code', 'used']


class SocialProgramSerializer(ModelSerializer):
    class Meta:
        model = SocialProgram
        fields = ['id', 'name', 'enabled']


class MaritalStatusSerializer(ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ['id', 'name', 'enabled']


class BenefitedSerializer(ModelSerializer):
    city = CitySerializer(read_only=True)
    marital_status = MaritalStatusSerializer(read_only=True)

    class Meta:
        model = Benefited
        fields = ['id', 'name', 'email', 'birth_date', 'child_count', 'monthly_familiar_income', 'has_disablement',
                  'marital_status', 'city']
