#  coding: utf-8
from django.urls import path

from core.views import AccessCodeGenericViews, AccessCodeSpecificViews

urlpatterns = [
    path("access_codes", AccessCodeGenericViews.as_view()),
    path("access_codes/<int:pk>", AccessCodeSpecificViews.as_view()),
]
