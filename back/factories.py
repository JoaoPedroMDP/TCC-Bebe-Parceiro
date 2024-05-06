#  coding: utf-8
import factory
from django.contrib.auth.models import Group, Permission
from factory.django import DjangoModelFactory
from faker import Faker

from config import ROLE_BENEFICIARY
from core.models import (
    User, Country, State, City, AccessCode,
    MaritalStatus, SocialProgram, Beneficiary, Volunteer, Campaign, Child, Size, Status, Swap,
    Speciality, Professional, Appointment, Register
)

fake = Faker()


class TimestampedModelFactory(DjangoModelFactory):
    created_at = factory.Faker('date_time_this_decade', tzinfo=None)
    updated_at = factory.Faker('date_time_this_decade', tzinfo=None)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
    password = factory.Faker('password')
    username = factory.Faker('phone_number')
    first_name = factory.Faker('first_name')

    @staticmethod
    def create(**kwargs):
        user_data = UserFactory.build(**kwargs)
        user = User.objects.create_user(**{
                "username": user_data.username,
                "email": user_data.email,
                "password": user_data.password,
                "first_name": user_data.first_name,
                "phone": user_data.phone
            }
        )

        return user


class EnablableModelFactory(TimestampedModelFactory):
    enabled = factory.Faker('boolean')


class CountryFactory(EnablableModelFactory):
    class Meta:
        model = Country

    name = factory.Faker('country')


class StateFactory(EnablableModelFactory):
    class Meta:
        model = State

    name = factory.Faker('state')
    country = factory.SubFactory(CountryFactory)


class CityFactory(EnablableModelFactory):
    class Meta:
        model = City

    name = factory.Faker('city')
    state = factory.SubFactory(StateFactory)


class AccessCodeFactory(TimestampedModelFactory):
    class Meta:
        model = AccessCode

    code = factory.Faker('pystr', max_chars=6)
    used = factory.Faker('boolean')


class MaritalStatusFactory(EnablableModelFactory):
    class Meta:
        model = MaritalStatus

    name = factory.Faker('random_element', elements=['Solteiro', 'Casado', 'Divorciado', 'Viúvo'])


class SocialProgramFactory(EnablableModelFactory):
    class Meta:
        model = SocialProgram

    name = factory.Faker(
        'random_element',
        elements=['CRAS', "Minha Casa Minha Vida", 'Cadastro de Emprego', 'Bolsa Família', 'Cartão alimentação']
    )


class BeneficiaryFactory(TimestampedModelFactory):
    class Meta:
        model = Beneficiary

    user = factory.SubFactory(UserFactory)
    marital_status = factory.Iterator(MaritalStatus.objects.all())
    city = factory.Iterator(City.objects.all())
    birth_date = factory.Faker('date_time_this_century', tzinfo=None)
    child_count = factory.Faker('random_int', min=0, max=10)
    monthly_familiar_income = factory.Faker('pydecimal', left_digits=5, right_digits=2)
    has_disablement = factory.Faker('boolean')


class VolunteerFactory(TimestampedModelFactory):
    class Meta:
        model = Volunteer

    user = factory.SubFactory(UserFactory)
    city = factory.SubFactory(CityFactory)


class CampaignFactory(TimestampedModelFactory):
    class Meta:
        model = Campaign

    name = factory.Faker('sentence', nb_words=4)
    start_date = factory.Faker('date_this_decade')
    end_date = factory.Faker('date_this_decade')
    description = factory.Faker('text')
    external_link = factory.Faker('url')


class ChildFactory(TimestampedModelFactory):
    class Meta:
        model = Child

    name = factory.Faker('first_name')
    birth_date = factory.Faker('date_time_this_decade', tzinfo=None)
    beneficiary = factory.SubFactory(BeneficiaryFactory)
    sex = factory.Faker('random_element', elements=['M', 'F'])


class SizeFactory(EnablableModelFactory):
    class Meta:
        model = Size

    name = factory.Faker('word')


class StatusFactory(EnablableModelFactory):
    class Meta:
        model = Status

    name = factory.Faker('word')


class SwapFactory(TimestampedModelFactory):
    class Meta:
        model = Swap

    cloth_size = factory.SubFactory(SizeFactory)
    shoe_size = factory.SubFactory(SizeFactory)
    description = factory.Faker('text')
    status = factory.SubFactory(StatusFactory)


class SpecialityFactory(EnablableModelFactory):
    class Meta:
        model = Speciality

    name = factory.Faker('word')


class ProfessionalFactory(EnablableModelFactory):
    class Meta:
        model = Professional

    name = factory.Faker('name')
    phone = factory.Faker('phone_number')
    speciality = factory.SubFactory(SpecialityFactory)
    accepted_volunteer_terms = factory.Faker('boolean')


class AppointmentFactory(TimestampedModelFactory):
    class Meta:
        model = Appointment

    beneficiary = factory.SubFactory(BeneficiaryFactory)
    volunteer = factory.SubFactory(VolunteerFactory)
    professional = factory.SubFactory(ProfessionalFactory)
    date = factory.Faker('date_this_year', tzinfo=None)
    time = factory.Faker('time', tzinfo=None)
    status = factory.SubFactory(StatusFactory)


class RegisterFactory(TimestampedModelFactory):
    class Meta:
        model = Register

    appointment = factory.SubFactory(AppointmentFactory)
    volunteer = factory.SubFactory(VolunteerFactory)
    beneficiary = factory.SubFactory(BeneficiaryFactory)
    description = factory.Faker('text')


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group
        skip_postgeneration_save = True

    name = factory.Faker('word')

    @factory.post_generation
    def permissions(self, create, extracted, **kwargs):
        if not create:
            return

        permissions = fake.random_choices(elements=Permission.objects.all(), length=3)
        for perm in permissions:
            self.permissions.add(perm)
