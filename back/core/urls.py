#  coding: utf-8
from django.conf.urls import include
from django.urls import path
from knox.views import LogoutView, LogoutAllView

from core.app_views.access_code_views import AccessCodeGenericViews, AccessCodeSpecificViews
from core.app_views.auth_views import LoginView
from core.app_views.benefited_views import BenefitedGenericViews, BenefitedSpecificViews
from core.app_views.child_views import ChildGenericViews, ChildSpecificViews
from core.app_views.city_views import CityGenericViews, CitySpecificViews
from core.app_views.country_views import CountryGenericViews, CountrySpecificViews
from core.app_views.marital_status_views import MaritalStatusGenericViews, MaritalStatusSpecificViews
from core.app_views.social_program_views import SocialProgramGenericViews, SocialProgramSpecificViews
from core.app_views.state_views import StateGenericViews, StateSpecificViews

# gen = generic
# spe = specific
# pk = primary key

urlpatterns = [
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),

    path("access_codes", AccessCodeGenericViews.as_view(), name="gen_access_codes"),
    path("access_codes/<int:pk>", AccessCodeSpecificViews.as_view(), name="spe_access_codes"),

    path("social_programs", SocialProgramGenericViews.as_view(), name="gen_social_programs"),
    path("social_programs/<int:pk>", SocialProgramSpecificViews.as_view(), name="spe_social_programs"),

    path("marital_statuses", MaritalStatusGenericViews.as_view(), name="gen_marital_statuses"),
    path("marital_statuses/<int:pk>", MaritalStatusSpecificViews.as_view(), name="spe_marital_statuses"),

    path("beneficiaries", BenefitedGenericViews.as_view(), name="gen_beneficiaries"),
    path("beneficiaries/<int:pk>", BenefitedSpecificViews.as_view(), name="spe_beneficiaries"),

    path("children", ChildGenericViews.as_view(), name="gen_children"),
    path("children/<int:pk>", ChildSpecificViews.as_view(), name="spe_children"),

    # Endereço
    path("countries", CountryGenericViews.as_view(), name="gen_countries"),
    path("countries/<int:pk>", CountrySpecificViews.as_view(), name="spe_countries"),

    path("states", StateGenericViews.as_view(), name="gen_states"),
    path("states/<int:pk>", StateSpecificViews.as_view(), name="spe_states"),

    path("cities", CityGenericViews.as_view(), name="gen_cities"),
    path("cities/<int:pk>", CitySpecificViews.as_view(), name="spe_cities"),
]
