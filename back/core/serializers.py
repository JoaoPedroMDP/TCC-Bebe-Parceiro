#  coding: utf-8
from rest_framework.serializers import ModelSerializer, SlugRelatedField, DateField

from core.models import Country, State, City, User
from core.models import AccessCode, SocialProgram, MaritalStatus, Beneficiary, Child


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'enabled']


class StateSerializer(ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = State
        fields = ['id', 'name', 'country', 'enabled']


class CitySerializer(ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'state', 'enabled']


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


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone']


class BenefitedSerializer(ModelSerializer):
    city = CitySerializer(read_only=True)
    marital_status = MaritalStatusSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Beneficiary
        fields = ['id', 'user', 'birth_date', 'child_count', 'monthly_familiar_income', 'has_disablement',
                  'marital_status', 'city']


class ChildSerializer(ModelSerializer):
    benefited = SlugRelatedField(slug_field='id', read_only=True)
    birth_date = DateField(format="%d/%m/%Y")

    class Meta:
        model = Child
        fields = ['id', 'name', 'birth_date', 'sex', 'benefited']
