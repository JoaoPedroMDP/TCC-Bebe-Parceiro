from django.db import models

from core.utils.dictable import Dictable


class BaseModel(models.Model, Dictable):
    readable_name = None
    objects = models.Manager()

    class Meta:
        abstract = True


class TimestampedModel(BaseModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimestampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30)

    class Meta:
        abstract = True


class LoggableUser(User):
    password = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Country(TimestampedModel):
    readable_name = "País"
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"<País: {self.name}>"


class State(TimestampedModel):
    readable_name = "Estado"
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Estado: {self.name}>"


class City(TimestampedModel):
    readable_name = "Cidade"
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Cidade: {self.name}>"


class AccessCode(TimestampedModel):
    readable_name = "Código de acesso"
    code = models.CharField(max_length=20, unique=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"<Código: {self.code}, Usado: {self.used}>"


class MaritalStatus(TimestampedModel):
    readable_name = "Estado civil"
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"<Estado civil: {self.name}>"


class SocialProgram(TimestampedModel):
    readable_name = "Programa social"
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"<Programa social: {self.name} - Habilitado: {self.enabled}"


# TODO: Trocar para Beneficiary
class Benefited(LoggableUser):
    readable_name = "Beneficiada"
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    social_programs = models.ManyToManyField(SocialProgram)

    birth_date = models.DateTimeField()
    child_count = models.IntegerField()
    monthly_familiar_income = models.DecimalField(max_digits=10, decimal_places=2)
    has_disablement = models.BooleanField(default=False)


class Volunteer(LoggableUser):
    readable_name = "Voluntária"
    role = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Campaign(TimestampedModel):
    readable_name = "Campanha"
    name: models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class Child(TimestampedModel):
    readable_name = "Filho/a"
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    benefited = models.ForeignKey(Benefited, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1)


class Size(TimestampedModel):
    readable_name = "Tamanho"
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)


class Status(TimestampedModel):
    readable_name = "Status"
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)


class Swap(TimestampedModel):
    """Troca de roupas"""
    readable_name = "Troca"
    cloth_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="clothes")
    shoe_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="shoes", null=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class Speciality(TimestampedModel):
    readable_name = "Especialidade"
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)


class Professional(User):
    readable_name = "Profissional"
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    accepted_volunteer_terms = models.BooleanField(default=False)


class Appointment(TimestampedModel):
    readable_name = "Agendamento"
    swap = models.ForeignKey(Swap, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Benefited, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True)

    date = models.DateField(null=True)
    hour = models.TimeField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class Register(TimestampedModel):
    readable_name = "Registro do prontuário"
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Benefited, on_delete=models.CASCADE)
    description = models.TextField()
