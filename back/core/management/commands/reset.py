#  coding: utf-8
import os
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection

from config import ENV, PROD


class Command(BaseCommand):
    help = 'Deleta o shema public, deleta a migration, reconstrói tudo de novo e depois popula com dados de teste'

    def handle(self, *app_labels, **options):
        if ENV == PROD:
            print("Não é possível rodar este comando em produção")
            return

        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE;")
            cursor.execute("CREATE SCHEMA public;")

        try:
            path = __file__.split('management')[0] + 'migrations/0001_initial.py'
            os.remove(path)
            print(f"{path} removido.")
        except FileNotFoundError:
            print("Arquivo não existia")
            pass

        call_command('makemigrations')
        call_command('migrate')
        call_command('seed')
