from django.core.management import BaseCommand, CommandError
from products.models import Products, Category, ProductCategories
import os
import json


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str)

    def handle(self, *args, **options):
        file_path = options.get('file')
        if not file_path:
            raise CommandError('File not provided')
        if not file_path.endswith('.json'):
            raise CommandError('Only .json files supported')

        file_path = os.path.join('data', file_path)
        try:
            with open(file_path) as import_file:
                products = json.load(import_file)
        except FileNotFoundError as e:
            raise CommandError('File at %s not found:' % os.path.join('data', file_path))

        db_products = Products.objects.all()
        db_categories = Category.objects.all()

        for data in products:
            for prod in db_products:
                if str(data['name']) == str(prod):
                    print(prod, prod.id, data['category'])
                    for i in data['category']:
                        for cat in db_categories:
                            if str(i['name']) == str(cat):
                                print(cat.name, cat.id)
                                db_product_categories = ProductCategories(
                                   product=prod,
                                   category=cat,
                                   )
                                db_product_categories.save()

