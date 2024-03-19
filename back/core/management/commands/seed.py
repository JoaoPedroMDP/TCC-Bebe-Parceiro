#  coding: utf-8
from datetime import timedelta
from random import randint
from typing import List

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from config import GROUPS
from core.models import User
from factories import MaritalStatusFactory, SocialProgramFactory, CountryFactory, StateFactory, CityFactory, \
    AccessCodeFactory, UserFactory, BeneficiaryFactory, ChildFactory, VolunteerFactory, GroupFactory


class Command(BaseCommand):
    help = 'Popula as tabelas com dados iniciais'
    # Valores base para alguns cruds
    MARITAL_STATUSES = ['Solteiro', 'Casado', 'Divorciado', 'Viúvo']
    SOCIAL_PROGRAMS = ['CRAS', "Minha Casa Minha Vida", 'Cadastro de Emprego', 'Bolsa Família', 'Cartão alimentação']

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

        if not options['test']:
            return

        # Estados civis e programas sociais
        for m in self.MARITAL_STATUSES:
            MaritalStatusFactory.create(name=m, enabled=True)

        for s in self.SOCIAL_PROGRAMS:
            SocialProgramFactory.create(name=s, enabled=True)

        # Beneficiárias com filhos nascidos
        for i in range(2):
            identification = f"ben_child_{i}"
            u: User = UserFactory.create(username=identification, password=identification, first_name=identification)

            b = BeneficiaryFactory.create(user=u)
            ChildFactory.create(beneficiary=b)

        # Beneficiárias grávidas
        for i in range(2):
            identification = f"ben_pregnant_{i}"
            u: User = UserFactory.create(username=identification, password=identification, first_name=identification)

            bdate = now() + timedelta(weeks=randint(3, 49))
            b = BeneficiaryFactory.create(user=u)
            ChildFactory.create(beneficiary=b, birth_date=bdate)

        # Uma voluntária pra cada cargo
        for g in groups:
            identification = f"vol_{g.name}"
            u: User = UserFactory.create(username=identification, password=identification, first_name=identification)
            u.groups.set([g])
            VolunteerFactory.create(user=u)

        # E uma voluntária admin
        admin_user = UserFactory.create(username="admin", password="admin", first_name="Isabela")
        admin_user.groups.set(groups)
        VolunteerFactory.create(user=admin_user)

        AccessCodeFactory.create_batch(5, used=False)
