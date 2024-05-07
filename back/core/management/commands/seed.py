#  coding: utf-8
from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from config import GROUPS, ROLE_PENDING_BENEFICIARY, ROLES, ROLE_BENEFICIARY, ROLE_VOLUNTEER, STATUSES, \
    MARITAL_STATUSES, SOCIAL_PROGRAMS
from core.models import User
from factories import MaritalStatusFactory, SocialProgramFactory, CountryFactory, StateFactory, CityFactory, \
    AccessCodeFactory, UserFactory, BeneficiaryFactory, ChildFactory, VolunteerFactory, GroupFactory, StatusFactory, \
    CampaignFactory


class Command(BaseCommand):
    help = 'Popula as tabelas com dados iniciais'

    def add_arguments(self, parser):
        parser.add_argument("--test", action='store_true', help="Se deve criar dados para testes manuais")

    def handle(self, *app_labels, **options):
        # CEP
        brazil = CountryFactory.create(name="Brasil", enabled=True)
        parana = StateFactory.create(name="Paraná", country=brazil, enabled=True)
        CityFactory.create(name="Maringá", state=parana, enabled=True)

        # Cargos e permissoes
        groups = []
        for g in GROUPS:
            groups.append(GroupFactory.create(name=g))

        roles = {}
        for r in ROLES:
            roles[r] = GroupFactory.create(name=r)

        if not options['test']:
            return

        # Estados civis
        for m in MARITAL_STATUSES:
            MaritalStatusFactory.create(name=m, enabled=True)

        # Programas sociais
        for s in SOCIAL_PROGRAMS:
            SocialProgramFactory.create(name=s, enabled=True)

        # Status
        for s in STATUSES:
            StatusFactory.create(name=s, enabled=True)

        # Beneficiárias esperando por aprovação
        for i in range(5):
            identification = f"ben_pending_{i}"
            u: User = UserFactory.create(username=identification, password=identification, first_name=identification)
            u.groups.add(roles[ROLE_PENDING_BENEFICIARY])

            BeneficiaryFactory.create(user=u)

        # Beneficiárias com filhos nascidos
        for i in range(2):
            identification = f"ben_child_{i}"
            u: User = UserFactory.create(username=identification, password=identification, first_name=identification)
            u.groups.add(roles[ROLE_BENEFICIARY])

            b = BeneficiaryFactory.create(user=u)
            ChildFactory.create(beneficiary=b)

        # Beneficiárias grávidas
        for i in range(2):
            identification = f"ben_pregnant_{i}"
            u: User = UserFactory.create(username=identification, password=identification, first_name=identification)
            u.groups.add(roles[ROLE_BENEFICIARY])

            bdate = now() + timedelta(weeks=randint(3, 49))
            b = BeneficiaryFactory.create(user=u)
            ChildFactory.create(beneficiary=b, birth_date=bdate)

        # Beneficiárias com programas sociais
        for i in range(2):
            identification = f"ben_social_{i}"
            u: User = UserFactory.create(username=identification, password=identification, first_name=identification)
            u.groups.add(roles[ROLE_BENEFICIARY])

            b = BeneficiaryFactory.create(user=u)
            b.social_programs.add(*SocialProgramFactory.create_batch(2))

        # Uma voluntária pra cada cargo
        for g in groups:
            identification = f"vol_{g.name}"
            u: User = UserFactory.create(username=identification, password=identification, first_name=identification)
            u.groups.set([g, roles[ROLE_VOLUNTEER]])
            VolunteerFactory.create(user=u)

        # E uma voluntária admin
        admin_user = UserFactory.create(username="admin", password="admin", first_name="Isabela")
        admin_user.groups.set([*groups, roles[ROLE_VOLUNTEER]])
        VolunteerFactory.create(user=admin_user)

        AccessCodeFactory.create_batch(5, used=False)
        CampaignFactory.create_batch(5)
