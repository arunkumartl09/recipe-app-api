from django.core.management.base import BaseCommand

import time

from psycopg2 import OperationalError as Psycopg2opError

from django.db.utils import OperationalError

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('waiting for database....')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])

                db_up = True
            except (Psycopg2opError, OperationalError):
                self.stdout.write('Database unavailabe , wait for one sec..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available!'))
