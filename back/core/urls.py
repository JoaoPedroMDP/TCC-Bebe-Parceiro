#  coding: utf-8
from django.urls import path

from core.views import AccessCodeGenericView

urlpatterns = [
    path("access_codes", AccessCodeGenericView.as_view()),
]
