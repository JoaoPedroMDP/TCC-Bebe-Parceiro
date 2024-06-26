#  coding: utf-8
from typing import List

from django.contrib.auth.models import Group, Permission
from rest_framework.fields import SerializerMethodField, DateTimeField
from rest_framework.serializers import ModelSerializer, SlugRelatedField, DateField

from core.models import (Country, Campaign, Register, Size, State, City, Status, Swap, User, Volunteer, Professional, Speciality,
                         AccessCode, SocialProgram, MaritalStatus, Beneficiary, Child, Appointment)


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
    class Meta:
        model = Group
        fields = ['id', 'name', 'description']


class UserSerializer(ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    role = SerializerMethodField()

    @staticmethod
    def get_role(obj: User) -> str:
        return obj.role

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'phone', 'groups', 'role']


class ChildSerializer(ModelSerializer):
    beneficiary_id = SlugRelatedField(slug_field='id', read_only=True, source='beneficiary')
    birth_date = DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Child
        fields = ['id', 'name', 'birth_date', 'sex', 'beneficiary_id']


class BeneficiarySerializer(ModelSerializer):
    marital_status = MaritalStatusSerializer(many=False, read_only=True)
    social_programs = SocialProgramSerializer(many=True, read_only=True)
    children = ChildSerializer(many=True, read_only=True)
    user = UserSerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    birth_date = DateTimeField(format="%Y-%m-%d")
    is_pregnant = SerializerMethodField()

    @staticmethod
    def get_is_pregnant(obj: Beneficiary) -> bool:
        return obj.is_pregnant()

    class Meta:
        model = Beneficiary
        fields = ['id', 'user', 'birth_date', 'child_count', 'monthly_familiar_income',
                  'has_disablement', 'marital_status', 'children', 'city', 'social_programs',
                  'approved', 'created_at', 'is_pregnant']


class VolunteerSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = Volunteer
        fields = ['id', 'user', 'city']


class SpecialitySerializer(ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'name', 'enabled']


class ProfessionalSerializer(ModelSerializer):
    speciality = SpecialitySerializer(read_only=True)
   
    class Meta:
        model = Professional
        fields = ['id', 'name', 'phone', 'speciality', 'accepted_volunteer_terms', 'enabled', 'approved']


class CampaignSerializer(ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'name', 'start_date', 'end_date', 'description', 'external_link']

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'enabled', 'type']


class StatusSerializer(ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'name', 'enabled']

class SwapSerializer(ModelSerializer):
    beneficiary = BeneficiarySerializer(read_only=True)
    cloth_size = SizeSerializer()
    shoe_size = SizeSerializer()
    child = ChildSerializer()
    status = StatusSerializer()
    
    class Meta:
        model = Swap
        fields = ['id', 'cloth_size', 'shoe_size', 'description', 'status', 'beneficiary', 'child', 'created_at']

class AppointmentSerializer(ModelSerializer):

    speciality = SpecialitySerializer(read_only=True)
    professional = ProfessionalSerializer(read_only=True)
    beneficiary = BeneficiarySerializer(read_only=True)
    volunteer = VolunteerSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'beneficiary', 'professional', 'speciality', 'volunteer', 'status', 'datetime']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'description']
