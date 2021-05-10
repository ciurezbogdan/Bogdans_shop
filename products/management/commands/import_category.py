from django.core.management import BaseCommand, CommandError
import os
import json
from products.models import Category


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str)

    def handle(self, *args, **options):
        file_path = options.get('file')
        if not file_path:
            raise CommandError('File not provided')
        if not file_path.endswith('.json'):
            raise CommandError('Only .json file supported')

        file_path = os.path.join('data', file_path)
        try:
            with open(file_path) as import_file:
                categories = json.load(import_file)
        except FileNotFoundError as e:
            raise CommandError('File at %s not found: ' % os.path.join('data', file_path))

        for category in categories:
            db_categories = Category(
                name=category['name']
            )
            db_categories.save()

