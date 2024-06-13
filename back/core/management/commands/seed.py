#  coding: utf-8
from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from config import CLOTH_SIZES, CLOTH_TYPE, GROUPS, MANAGE_EVALUATIONS, SHOE_SIZES, SHOE_TYPE, STATUSES, MARITAL_STATUSES, SOCIAL_PROGRAMS
from core.management.commands import ADMIN_DATA, APPROVED_BENEFICIARIES, PENDING_BENEFICIARIES, SWAP_BENEFICIARIES, VOLUNTEERS
from core.models import Beneficiary, Child, City, MaritalStatus, SocialProgram, User, Volunteer
from factories import AppointmentFactory, MaritalStatusFactory, RegisterFactory, SocialProgramFactory, SizeFactory, CountryFactory, StateFactory, CityFactory, \
    AccessCodeFactory, SwapFactory, UserFactory, BeneficiaryFactory, ChildFactory, VolunteerFactory, GroupFactory, StatusFactory, CampaignFactory


class Command(BaseCommand):
    help = 'Popula as tabelas com dados iniciais'

    def add_arguments(self, parser):
        parser.add_argument("--test", action='store_true', help="Se deve criar dados para testes manuais")

    @staticmethod
    def create_beneficiary(ben: dict, cities: list[City], mar_stats: list[MaritalStatus], soc_progs: list[SocialProgram]):
        u = UserFactory.create(**ben['user'])
        ben['user'] = u
        ben['city'] = cities[ben['city']]
        marital_status = mar_stats[ben.pop('marital_status')]
        social_programs = [soc_progs[s] for s in ben.pop('social_programs')]

        children_data = ben.pop('children_data')
        
        b = BeneficiaryFactory.create(**ben)
        b.marital_status = marital_status
        b.social_programs.set(social_programs)

        children = []
        for child_data in children_data:
            children.append(ChildFactory.create(beneficiary=b, **child_data))
        
        return b, children

    @staticmethod
    def create_swap(swap: dict, beneficiary: Beneficiary, child: Child, shoe_sizes: dict, cloth_sizes: dict, statuses: dict):
        swap['beneficiary'] = beneficiary
        swap['child'] = child
        swap['cloth_size'] = cloth_sizes[swap.pop('cloth_size')]
        if 'shoe_size' in swap:
            swap['shoe_size'] = shoe_sizes[swap.pop('shoe_size')]
        swap['status'] = statuses[swap.pop('status')]
        SwapFactory.create(**swap)

    def create_appointment(self, beneficiary: Beneficiary, volunteer: Volunteer, appointment: dict):
        appointment['beneficiary'] = beneficiary
        appointment['volunteer'] = volunteer
        return AppointmentFactory.create(**appointment)

    def create_register(self, register: dict, beneficiary: Beneficiary, volunteer: Volunteer):
        register['beneficiary'] = beneficiary
        register['appointment'] = self.create_appointment(beneficiary, volunteer, register.pop('appointment'))
        register['volunteer'] = volunteer
        RegisterFactory.create(**register)
    
    def handle(self, *app_labels, **options):
        # CEP
        brazil = CountryFactory.create(name="Brasil", enabled=True)
        parana = StateFactory.create(name="Paraná", country=brazil, enabled=True)
        cities = {
            "maringa": CityFactory.create(name="Maringá", state=parana, enabled=True),
            "umuarama": CityFactory.create(name="Umuarama", state=parana, enabled=True),
            "sarandi": CityFactory.create(name="Sarandi", state=parana, enabled=True),
            "iguatemi": CityFactory.create(name="Iguatemi", state=parana, enabled=True),
        }

        # Cargos e permissoes
        groups = []
        for g in GROUPS:
            groups.append(GroupFactory.create(name=g))

        # Estados civis
        mar_stats = {}
        for m in MARITAL_STATUSES:
            mar_stats[m] = MaritalStatusFactory.create(name=m, enabled=True)

        # Programas sociais
        soc_progs = {}
        for s in SOCIAL_PROGRAMS:
            soc_progs[s] = SocialProgramFactory.create(name=s, enabled=True)

        # Status
        statuses = {}
        for s in STATUSES:
            statuses[s] = StatusFactory.create(name=s, enabled=True)
        
        # Tamanhos de sapato
        shoe_sizes = {}
        for s in SHOE_SIZES:
            shoe_sizes[s] = SizeFactory.create(name=s, type=SHOE_TYPE)
        
        # Tamanhos de roupa
        cloth_sizes = {}
        for s in CLOTH_SIZES:
            cloth_sizes[s] = SizeFactory.create(name=s, type=CLOTH_TYPE)
        
        admin_user = UserFactory.create(**ADMIN_DATA)
        admin_user.groups.set(groups)
        VolunteerFactory.create(user=admin_user, city=cities['maringa'])
        
        volunteers = {}
        for i, group in enumerate(GROUPS):
            vol = VOLUNTEERS[i]
            u: User = UserFactory.create(**vol['user'])
            
            vol['city'] = cities[vol['city']]
            volunteers[group] = VolunteerFactory.create(user=u)

        for ben in PENDING_BENEFICIARIES:
            registers = []
            if 'registers' in ben:
                registers = ben.pop('registers')

            pending_ben, _ = self.create_beneficiary(ben, cities, mar_stats, soc_progs)

            for r in registers:
                self.create_register(r, pending_ben, volunteers[MANAGE_EVALUATIONS])

        for ben in APPROVED_BENEFICIARIES:
            self.create_beneficiary(ben, cities, mar_stats, soc_progs)

        for ben in SWAP_BENEFICIARIES:
            swap_data = ben.pop("swap_data")
            ben, children = self.create_beneficiary(ben, cities, mar_stats, soc_progs)
            self.create_swap(swap_data, ben, children[0], shoe_sizes, cloth_sizes, statuses)
