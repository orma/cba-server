import sys
import os.path as osp

from django.core.management.base import BaseCommand

from administrations import utils


class Command(BaseCommand):
    help = 'Import provinces data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--json_file',
            dest='json_file',
            required=True,
            help='JSON file containing all provinces and districts'
        )

    def handle(self, *args, **options):
        json_file = options['json_file']

        if not osp.exists(json_file):
            self.stderr.write(self.style.ERROR('File not found {}'.format(json_file)))
            sys.exit(1)

        utils.import_admin_unit(json_file)        
