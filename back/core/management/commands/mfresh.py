#  coding: utf-8
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Deleta todas as tabelas e as constrói denovo'

    def handle(self, *app_labels, **options):
        tables = connection.introspection.table_names()

        connection.disable_constraint_checking()

        schema_editor = connection.schema_editor()
        schema_editor.execute(schema_editor.sql_delete_table % {
            'table': ','.join(tables)
        })

        connection.enable_constraint_checking()

        call_command('migrate')
