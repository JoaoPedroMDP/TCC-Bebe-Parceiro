#  coding: utf-8
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
