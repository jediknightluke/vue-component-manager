# core/management/commands/wait_for_db.py
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from authentication.models import CustomUser
from django.db import connections
import time
import os


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while db_conn is None:
            try:
                # Print the connection details
                self.stdout.write(f"Attempting to connect to database with following details: ")
                self.stdout.write(f"DJANGO_DB_ENGINE: {os.getenv('DJANGO_DB_ENGINE')}")
                self.stdout.write(f"DJANGO_DB_NAME: {os.getenv('DJANGO_DB_NAME')}")
                self.stdout.write(f"DJANGO_DB_USER: {os.getenv('DJANGO_DB_USER')}")
                self.stdout.write(f"DJANGO_DB_PASSWORD: {os.getenv('DJANGO_DB_PASSWORD')}")
                self.stdout.write(f"DJANGO_DB_HOST: {os.getenv('DJANGO_DB_HOST')}")
                self.stdout.write(f"DJANGO_DB_PORT: {os.getenv('DJANGO_DB_PORT')}")

                # Attempt to execute a simple database operation
                db_conn = connections['default']
                db_conn.cursor().execute('SELECT 1')
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                db_conn = None
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
