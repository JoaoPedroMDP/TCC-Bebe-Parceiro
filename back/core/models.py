from django.db import models

# Alguns models estão nos arquivos importados aqui em cima para fins de melhor organização
from core.db_models.abstract_models import TimestampedModel, LoggableUser
from core.db_models.adress_related_models import City


class AccessCode(TimestampedModel):
    readable_name = "Código de acesso"
    code = models.CharField(max_length=20, unique=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"<Código: {self.code}, Usado: {self.used}>"


class MaritalStatus(TimestampedModel):
    readable_name = "Estado civil"
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"<Estado civil: {self.name}>"


class SocialProgram(TimestampedModel):
    readable_name = "Programa social"
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"<Programa social: {self.name} - Habilitado: {self.enabled}"


class BenefitedSocialProgram(TimestampedModel):
    benefited_id = models.ForeignKey('Benefited', on_delete=models.CASCADE)
    social_program_id = models.ForeignKey(SocialProgram, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Beneficiado: {self.benefited_id}, Programa social: {self.social_program_id}>"


class Benefited(LoggableUser):
    readable_name = "Beneficiada"
    marital_status_id = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    birth_date = models.DateField()
    child_count = models.IntegerField()
    mothly_familiar_income = models.DecimalField(max_digits=10, decimal_places=2)
    has_disablement = models.BooleanField(default=False)
