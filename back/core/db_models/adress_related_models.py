#  coding: utf-8
from django.db import models

from core.db_models.abstract_models import TimestampedModel


class Country(TimestampedModel):
    readable_name = "País"
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"<País: {self.name}>"


class State(TimestampedModel):
    readable_name = "Estado"
    name = models.CharField(max_length=255)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Estado: {self.name}>"


class City(TimestampedModel):
    readable_name = "Cidade"
    name = models.CharField(max_length=255)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Cidade: {self.name}>"
