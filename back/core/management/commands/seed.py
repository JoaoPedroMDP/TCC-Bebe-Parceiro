#  coding: utf-8
from typing import List

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection

from core.models import User
from factories import MaritalStatusFactory, SocialProgramFactory, CountryFactory, StateFactory, CityFactory, \
    AccessCodeFactory, UserFactory, BeneficiaryFactory, ChildFactory


class Command(BaseCommand):
    help = 'Popula as tabelas com dados iniciais'
    # Valores base para alguns cruds
    MARITAL_STATUSES = ['Solteiro', 'Casado', 'Divorciado', 'Viúvo']
    SOCIAL_PROGRAMS = ['CRAS', "Minha Casa Minha Vida", 'Cadastro de Emprego', 'Bolsa Família', 'Cartão alimentação']

    def handle(self, *app_labels, **options):
        for m in self.MARITAL_STATUSES:
            print("Criando estado civil: {}".format(m))
            MaritalStatusFactory.create(name=m, enabled=True)

        for s in self.SOCIAL_PROGRAMS:
            print("Criando programa social: {}".format(s))
            SocialProgramFactory.create(name=s, enabled=True)

        print("Criando C.E.P iniciais")
        brazil = CountryFactory.create(name="Brasil", enabled=True)
        parana = StateFactory.create(name="Paraná", country=brazil, enabled=True)
        CityFactory.create(name="Maringá", state=parana, enabled=True)
        AccessCodeFactory.create_batch(5, used=False)

        users: List[User] = UserFactory.build_batch(5)
        for u in users:
            User.objects.create_user(
                username=u.username,
                password=u.password,
                first_name=u.first_name,
                last_name=u.last_name,
            )
        User.objects.create_user(username="teste", password="teste")

        BeneficiaryFactory.create_batch(5)
        ChildFactory.create_batch(5)
