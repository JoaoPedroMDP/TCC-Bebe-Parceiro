from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)

admin.site.register(MaritalStatus)
admin.site.register(SocialProgram)