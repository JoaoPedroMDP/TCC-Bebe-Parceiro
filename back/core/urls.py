#  coding: utf-8
from django.urls import path
from knox.views import LogoutView

from core.app_views.access_code_views import AccessCodeGenericViews, AccessCodeSpecificViews
from core.app_views.auth_views import LoginView
from core.app_views.beneficiary_views import BeneficiaryGenericViews, BeneficiarySpecificViews
from core.app_views.child_views import ChildGenericViews, ChildSpecificViews
from core.app_views.city_views import CityGenericViews, CitySpecificViews
from core.app_views.country_views import CountryGenericViews, CountrySpecificViews
from core.app_views.marital_status_views import MaritalStatusGenericViews, MaritalStatusSpecificViews
from core.app_views.social_program_views import SocialProgramGenericViews, SocialProgramSpecificViews
from core.app_views.state_views import StateGenericViews, StateSpecificViews
from core.app_views.volunteer_views import VolunteerGenericViews, VolunteerSpecificViews
from core.app_views.professional_views import ProfessionalGenericViews, ProfessionalSpecificViews
#from core.app_views.speciality_views import SpecialityGenericViews, SpecialitySpecificViews
# gen = generic
# spe = specific
# pk = primary key

# está em ordem alfabética
urlpatterns = [
    path("access_codes", AccessCodeGenericViews.as_view(), name="gen_access_codes"),
    path("access_codes/<int:pk>", AccessCodeSpecificViews.as_view(), name="spe_access_codes"),

    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),

    path("beneficiaries", BeneficiaryGenericViews.as_view(), name="gen_beneficiaries"),
    path("beneficiaries/<int:pk>", BeneficiarySpecificViews.as_view(), name="spe_beneficiaries"),

    path("children", ChildGenericViews.as_view(), name="gen_children"),
    path("children/<int:pk>", ChildSpecificViews.as_view(), name="spe_children"),

    path("cities", CityGenericViews.as_view(), name="gen_cities"),
    path("cities/<int:pk>", CitySpecificViews.as_view(), name="spe_cities"),

    path("countries", CountryGenericViews.as_view(), name="gen_countries"),
    path("countries/<int:pk>", CountrySpecificViews.as_view(), name="spe_countries"),

    path("marital_statuses", MaritalStatusGenericViews.as_view(), name="gen_marital_statuses"),
    path("marital_statuses/<int:pk>", MaritalStatusSpecificViews.as_view(), name="spe_marital_statuses"),

    path("social_programs", SocialProgramGenericViews.as_view(), name="gen_social_programs"),
    path("social_programs/<int:pk>", SocialProgramSpecificViews.as_view(), name="spe_social_programs"),

    path("states", StateGenericViews.as_view(), name="gen_states"),
    path("states/<int:pk>", StateSpecificViews.as_view(), name="spe_states"),

    path("volunteers", VolunteerGenericViews.as_view(), name="gen_volunteers"),
    path("volunteers/<int:pk>", VolunteerSpecificViews.as_view(), name="spe_volunteers"),

    path("professionals", ProfessionalGenericViews.as_view(), name="gen_professionals"),
    path("professionals/<int:pk>", ProfessionalSpecificViews.as_view(), name="spe_professionals"),

#    path("specialities", SpecialityGenericViews.as_view(), name="gen_specialities"),
#    path("specialities/<int:pk>", SpecialitySpecificViews.as_view(), name="spe_specialities"),
]
