#  coding: utf-8
from django.urls import path

from core.app_views.access_code_views import AccessCodeGenericViews, AccessCodeSpecificViews
from core.app_views.benefited_views import BenefitedGenericViews, BenefitedSpecificViews
from core.app_views.marital_status_views import MaritalStatusGenericViews, MaritalStatusSpecificViews
from core.app_views.social_program_views import SocialProgramGenericViews, SocialProgramSpecificViews
from core.app_views.country_views import CountryGenericViews, CountrySpecificViews
from core.app_views.state_views import StateGenericViews, StateSpecificViews
from core.app_views.city_views import CityGenericViews, CitySpecificViews


urlpatterns = [
    path("access_codes", AccessCodeGenericViews.as_view()),
    path("access_codes/<int:pk>", AccessCodeSpecificViews.as_view()),

    path("social_programs", SocialProgramGenericViews.as_view()),
    path("social_programs/<int:pk>", SocialProgramSpecificViews.as_view()),

    path("marital_statuses", MaritalStatusGenericViews.as_view()),
    path("marital_statuses/<int:pk>", MaritalStatusSpecificViews.as_view()),

    path("beneficiaries", BenefitedGenericViews.as_view()),
    path("beneficiaries/<int:pk>", BenefitedSpecificViews.as_view()),

    path("countries", CountryGenericViews.as_view()),
    path("countries/<int:pk>", CountrySpecificViews.as_view()),

    path("states", StateGenericViews.as_view()),
    path("states/<int:pk>", StateSpecificViews.as_view()),

    path("cities", CityGenericViews.as_view()),
    path("cities/<int:pk>", CitySpecificViews.as_view()),
]
