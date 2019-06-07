import sys
import csv
import os.path as osp
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """This command is used to import legacy province section data - the ones
    used in the original Excel CBA """
    help = 'Import section data (in legacy format)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv',
            dest='csv',
            help='The CSV file containing sections data'
        )

    def _import_sections(self, csv_path):
        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                print(line.keys())
                break

    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.SUCCESS('=== IMPORT SECTION DATA (Legacy) ===')
        )

        csv = kwargs.get('csv', None)
        if csv is None:
            self.stderr.write(
                self.style.ERROR('A csv file containing section data is required')
            )
        
        if not osp.exists(csv):
            self.stderr.write(
                self.style.ERROR('File: %s not found.' % csv)
            )
            sys.exit(1)
        
        self._import_sections(csv)
