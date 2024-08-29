"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:  # chek if db is up
            try:
                self.check(databases=['default'])  # if db not ready-exeption
                db_up = True  # if we got here so db is up
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)  # slepp for a second let db wake up

        self.stdout.write(self.style.SUCCESS('Database available!'))
