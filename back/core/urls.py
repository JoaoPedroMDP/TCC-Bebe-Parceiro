#  coding: utf-8
from django.urls import path

from core.app_views.access_code_views import AccessCodeGenericViews, AccessCodeSpecificViews
from core.app_views.marital_status_views import MaritalStatusGenericViews, MaritalStatusSpecificViews
from core.app_views.social_program_views import SocialProgramGenericViews, SocialProgramSpecificViews

urlpatterns = [
    path("access_codes", AccessCodeGenericViews.as_view()),
    path("access_codes/<int:pk>", AccessCodeSpecificViews.as_view()),

    path("social_programs", SocialProgramGenericViews.as_view()),
    path("social_programs/<int:pk>", SocialProgramSpecificViews.as_view()),

    path("marital_statuses", MaritalStatusGenericViews.as_view()),
    path("marital_statuses/<int:pk>", MaritalStatusSpecificViews.as_view()),
]
