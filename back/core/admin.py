from django.contrib import admin
from .db_models.adress_related_models import *
# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)