#  coding: utf-8
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Deleta todas as tabelas e as constrói denovo, depois popula com dados de teste'

    def handle(self, *app_labels, **options):
        call_command('mfresh')
        call_command('seed', '--test')
