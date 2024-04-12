#  coding: utf-8
from typing import List

from django.contrib.auth.models import Group, Permission
from rest_framework.fields import SerializerMethodField, DateTimeField
from rest_framework.serializers import ModelSerializer, SlugRelatedField, DateField

from core.models import (Country, State, City, User, Volunteer, Professional, Speciality,
                         AccessCode, SocialProgram, MaritalStatus, Beneficiary, Child)


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
        fields = ['id', 'name']


class MaritalStatusSerializer(ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ['id', 'name', 'enabled']


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name']


class GroupSerializer(ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']


class UserSerializer(ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    role = SerializerMethodField()

    def get_role(self, obj: User):
        def role_filter(group):
            return group.name.startswith('role_')

        groups: List = obj.groups.all()
        role = list(filter(role_filter, groups))
        if len(role) > 0:
            return role[0].name.split("_")[1]

        return "Unknown"

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'phone', 'groups', 'role']


class ChildSerializer(ModelSerializer):
    benefited_id = SlugRelatedField(slug_field='id', read_only=True, source='beneficiary')
    birth_date = DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Child
        fields = ['id', 'name', 'birth_date', 'sex', 'benefited_id']


class BeneficiarySerializer(ModelSerializer):
    city_id = SlugRelatedField(slug_field='id', read_only=True, source='city')
    marital_status_id = SlugRelatedField(slug_field='id', read_only=True, source='marital_status')
    social_programs = SocialProgramSerializer(many=True, read_only=True)
    children = ChildSerializer(many=True, read_only=True)
    birth_date = DateTimeField(format="%Y-%m-%d")

    name = SerializerMethodField()
    phone = SerializerMethodField()
    email = SerializerMethodField()

    class Meta:
        model = Beneficiary
        fields = ['id', 'name', 'phone', 'email', 'birth_date', 'child_count', 'monthly_familiar_income',
                  'has_disablement', 'marital_status_id', 'children', 'city_id', 'social_programs', 'created_at']

    def get_name(self, obj: Beneficiary):
        return obj.user.name

    def get_phone(self, obj: Beneficiary):
        return obj.user.phone

    def get_email(self, obj: Beneficiary):
        return obj.user.email


class VolunteerSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = Volunteer
        fields = ['id', 'user', 'city']


class SpecialitySerializer(ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'name']


class ProfessionalSerializer(ModelSerializer):
    speciality = SpecialitySerializer(read_only=True)
   

    class Meta:
        model = Professional
        fields = ['id', 'name', 'phone', 'speciality', 'accepted_volunteer_terms']

