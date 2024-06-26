import datetime
import logging
from typing import List
from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from config import PENDING
from core.utils.dictable import Dictable


lgr = logging.getLogger(__name__)


Group.add_to_class('description', models.CharField(max_length=300, null=True))

class BaseModel(models.Model, Dictable):
    readable_name = None
    # Este objects é só pra ajudar no autocomplete do PyCharm
    objects = models.Manager()

    class Meta:
        abstract = True


class TimestampedModel(BaseModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EnablableModel(TimestampedModel):
    enabled = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractUser, Dictable):
    readable_name = "Usuária"

    phone = models.CharField(max_length=30, null=False)

    @property
    def name(self):
        return self.first_name

    @name.setter
    def name(self, value):
        self.first_name = value

    @property
    def role(self) -> str:
        if self.is_beneficiary():
            return "beneficiary" if self.beneficiary.approved else "pending_beneficiary"

        return "volunteer"

    def is_beneficiary(self) -> bool:
        """
            Se for beneficiada, tentar acessar o atributo beneficiary não vai lançar exceção
        """
        try:
            if not isinstance(self.beneficiary, Beneficiary):
                self.beneficiary.get()
            
            return True
        except Beneficiary.DoesNotExist:
            return False

    def is_volunteer(self) -> bool:
        """
            Se for voluntária, tentar acessar o atributo volunteer não vai lançar exceção
        """
        try:
            if not isinstance(self.volunteer, Volunteer):
                self.volunteer.get()

            return True
        except Volunteer.DoesNotExist:
            return False


class Country(EnablableModel):
    readable_name = "País"

    name = models.CharField(max_length=255)

    def __str__(self):
        return f"<País: {self.name}>"


class State(EnablableModel):
    readable_name = "Estado"

    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")

    def __str__(self):
        return f"<Estado: {self.name}>"


class City(EnablableModel):
    readable_name = "Cidade"

    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
        return f"<Cidade: {self.name}>"


class AccessCode(TimestampedModel):
    readable_name = "Código de acesso"

    code = models.CharField(max_length=20, unique=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"<Código: {self.code}, Usado: {self.used}>"


class MaritalStatus(EnablableModel):
    readable_name = "Estado civil"

    name = models.CharField(max_length=255)

    def __str__(self):
        return f"<Estado civil: {self.name}>"


class SocialProgram(EnablableModel):
    readable_name = "Programa social"

    name = models.CharField(max_length=255)

    def __str__(self):
        return f"<Programa social: {self.name} - Habilitado: {self.enabled}"


class Beneficiary(TimestampedModel):
    readable_name = "Beneficiada"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="beneficiary")
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, related_name="beneficiaries")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="beneficiaries")
    social_programs = models.ManyToManyField(SocialProgram)

    birth_date = models.DateTimeField()
    child_count = models.IntegerField()
    monthly_familiar_income = models.DecimalField(max_digits=10, decimal_places=2)
    has_disablement = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def has_pending_swap(self):
        """
            Verifica se a beneficiária tem uma troca pendente
        """
        return self.swaps.filter(status__name=PENDING).exists()

    def have_children_born(self):
        """
            Verifica se a beneficiária tem filhos nascidos
        """
        today = datetime.datetime.now()
        return self.children.filter(birth_date__lte=today).exists()

    def is_pregnant(self):
        """
            Verifica se a beneficiária está grávida
        """
        today = datetime.datetime.now()
        return self.children.filter(birth_date__gt=today).exists()

class Volunteer(TimestampedModel):
    readable_name = "Voluntária"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="volunteer")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="volunteers")


class Campaign(TimestampedModel):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    external_link = models.CharField(max_length=500, null=True)


class Child(TimestampedModel):
    readable_name = "Filho/a"

    name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name="children")
    sex = models.CharField(max_length=1)

    @property
    def age(self):
        today = datetime.datetime.now()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Size(EnablableModel):
    readable_name = "Tamanho"

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class Status(EnablableModel):
    readable_name = "Status"

    name = models.CharField(max_length=255)


class Swap(TimestampedModel):
    """Troca de roupas"""
    readable_name = "Troca"

    cloth_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="clothes")
    shoe_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="shoes", null=True)
    description = models.TextField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name="swaps")
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="swaps")

class Speciality(EnablableModel):
    readable_name = "Especialidade"

    name = models.CharField(max_length=255)


class Professional(EnablableModel):
    readable_name = "Profissional"

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    approved = models.BooleanField(default=False)

    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="professionals")
    accepted_volunteer_terms = models.BooleanField(default=False)


class Appointment(TimestampedModel):
    readable_name = "Agendamento"

    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name="appointments")
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True, related_name="appointments")
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True, related_name="appointments")
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, null=True, related_name="appointments")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="appointments")

    datetime = models.DateTimeField(null=True)


class Register(TimestampedModel):
    readable_name = "Registro do prontuário"

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="registers")
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name="registers")
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name="registers")
    description = models.TextField()
