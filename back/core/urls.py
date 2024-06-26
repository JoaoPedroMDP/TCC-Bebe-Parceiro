#  coding: utf-8
from django.urls import path
from knox.views import LogoutView

from core.app_views.access_code_views import AccessCodeGenericViews, AccessCodeSpecificViews, CheckAccessCodeView
from core.app_views.appointment_views import AppointmentGenericViews, AppointmentSpecificViews, EndEvaluationViews, ListAssignedEvaluationsViews, AppointmentReportsView
from core.app_views.auth_views import LoginView, GroupGenericView
from core.app_views.beneficiary_views import BeneficiaryCanRequestSwapView, BeneficiaryGenericViews, BeneficiaryReportsView, BeneficiarySpecificViews, \
    BeneficiaryCreationByVolunteerView, BeneficiaryApprovalView, BeneficiaryPendingView
from core.app_views.campaign_views import CampaignGenericViews, CampaignSpecificViews, OpenCampaignsView
from core.app_views.child_views import ChildGenericViews, ChildSpecificViews
from core.app_views.city_views import CityGenericViews, CitySpecificViews
from core.app_views.country_views import CountryGenericViews, CountrySpecificViews
from core.app_views.marital_status_views import MaritalStatusGenericViews, MaritalStatusSpecificViews
from core.app_views.register_views import RegisterGenericView, RegisterSpecificView
from core.app_views.size_views import SizeGenericViews, SizeSpecificViews
from core.app_views.social_program_views import SocialProgramGenericViews, SocialProgramSpecificViews
from core.app_views.state_views import StateGenericViews, StateSpecificViews
from core.app_views.status_views import StatusGenericViews, StatusSpecificViews
from core.app_views.swap_views import SwapGenericViews, SwapReportsView, SwapSpecificViews
from core.app_views.volunteer_views import VolunteerGenericViews, VolunteerReportsView, VolunteerSpecificViews, VolunteerEvaluatorsViews
from core.app_views.professional_views import ProfessionalGenericViews, ProfessionalSpecificViews
from core.app_views.speciality_views import SpecialityGenericViews, SpecialitySpecificViews
# gen = generic
# spe = specific
# pk = primary key

# está em ordem alfabética
urlpatterns = [
    path("access_codes", AccessCodeGenericViews.as_view(), name="gen_access_codes"), # Possui teste
    path("access_codes/<int:pk>", AccessCodeSpecificViews.as_view(), name="spe_access_codes"), # Possui teste
    path("access_codes/check", CheckAccessCodeView.as_view(), name="check_access_code"), # Possui teste

    path("appointments", AppointmentGenericViews.as_view(), name="gen_appointments"),
    path("appointments/<int:pk>", AppointmentSpecificViews.as_view(), name="spe_appointments"),
    path("appointments/reports", AppointmentReportsView.as_view(), name="reports_appointments"),
    path("appointments/assigned_evaluations", ListAssignedEvaluationsViews.as_view(), name="assigned_evaluations"),
    path("appointments/end_evaluation/<int:pk>", EndEvaluationViews.as_view(), name="end_evaluation"),

    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('auth/groups', GroupGenericView.as_view(), name='gen_groups'),

    path("beneficiaries", BeneficiaryGenericViews.as_view(), name="gen_beneficiaries"), # Possui teste
    path("beneficiaries/<int:pk>", BeneficiarySpecificViews.as_view(), name="spe_beneficiaries"), # Possui teste
    path("beneficiaries/approve/<int:pk>", BeneficiaryApprovalView.as_view(), name="approve_beneficiaries"), # Possui teste
    path("beneficiaries/create", BeneficiaryCreationByVolunteerView.as_view(), name="create_beneficiaries"), # Possui teste
    path("beneficiaries/pending", BeneficiaryPendingView.as_view(), name="pending_beneficiaries"), # Possui teste
    path("beneficiaries/can_request_swap", BeneficiaryCanRequestSwapView.as_view(), name="can_request_swap_beneficiaries"), # Possui teste
    path("beneficiaries/reports", BeneficiaryReportsView.as_view(), name="reports_beneficiaries"),
     
    path("campaigns", CampaignGenericViews.as_view(), name="gen_campaigns"),
    path("campaigns/<int:pk>", CampaignSpecificViews.as_view(), name="spe_campaigns"),
    path("campaigns/open", OpenCampaignsView.as_view(), name="open_campaigns"),

    path("children", ChildGenericViews.as_view(), name="gen_children"),
    path("children/<int:pk>", ChildSpecificViews.as_view(), name="spe_children"),

    path("cities", CityGenericViews.as_view(), name="gen_cities"),
    path("cities/<int:pk>", CitySpecificViews.as_view(), name="spe_cities"),

    path("countries", CountryGenericViews.as_view(), name="gen_countries"),
    path("countries/<int:pk>", CountrySpecificViews.as_view(), name="spe_countries"),

    path("marital_statuses", MaritalStatusGenericViews.as_view(), name="gen_marital_statuses"),
    path("marital_statuses/<int:pk>", MaritalStatusSpecificViews.as_view(), name="spe_marital_statuses"),

    path("professionals", ProfessionalGenericViews.as_view(), name="gen_professionals"),
    path("professionals/<int:pk>", ProfessionalSpecificViews.as_view(), name="spe_professionals"),

    path("registers", RegisterGenericView.as_view(), name="gen_registers"),
    path("registers/<int:pk>", RegisterSpecificView.as_view(), name="spe_registers"),

    path("social_programs", SocialProgramGenericViews.as_view(), name="gen_social_programs"),
    path("social_programs/<int:pk>", SocialProgramSpecificViews.as_view(), name="spe_social_programs"),

    path("specialities", SpecialityGenericViews.as_view(), name="gen_specialities"),
    path("specialities/<int:pk>", SpecialitySpecificViews.as_view(), name="spe_specialities"),

    path("states", StateGenericViews.as_view(), name="gen_states"),
    path("states/<int:pk>", StateSpecificViews.as_view(), name="spe_states"),

    path("volunteers", VolunteerGenericViews.as_view(), name="gen_volunteers"),
    path("volunteers/<int:pk>", VolunteerSpecificViews.as_view(), name="spe_volunteers"),
    path("volunteers/evaluators", VolunteerEvaluatorsViews.as_view(), name="spe_volunteers"),
    path("volunteers/reports", VolunteerReportsView.as_view(), name="reports_volunteers"),
 
    path("swaps", SwapGenericViews.as_view(), name="gen_swaps"),
    path("swaps/<int:pk>", SwapSpecificViews.as_view(), name="spe_swaps"),
    path("swaps/reports", SwapReportsView.as_view(), name="reports_swaps"),
 
    path("sizes", SizeGenericViews.as_view(), name="gen_sizes"),
    path("sizes/<int:pk>", SizeSpecificViews.as_view(), name="spe_sizes"),

    path("status", StatusGenericViews.as_view(), name="gen_status"),
    path("status/<int:pk>", StatusSpecificViews.as_view(), name="spe_status"),

]
