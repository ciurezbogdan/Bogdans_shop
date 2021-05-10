from django.core.management import BaseCommand, CommandError
from users.models import AuthUser
from products.models import Products, Category, ProductCategories
import os
import json


def get_category_list():
    with open(os.path.join('data', 'categories.json')) as categories_file:
        category_list = json.load(categories_file)
    return category_list


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
                print('products: ', products)
        except FileNotFoundError as e:
            raise CommandError('File at %s not found:' % os.path.join('data', file_path), e)

        for data in products:

            # import user data
            user = data['user']
            db_user = AuthUser.objects.create_user(
                first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                # password='python123'
            )
            print('db_user: ', db_user)

            # import products data
            db_product = Products(
                user=db_user,
                name=data['name'],
                description=data['description'],
                image=data['image'],
                price=data['price'],
                auction_price=data['auction_price'],
            )
            print(db_product)
            db_product.save()

            # category_list = get_category_list()
            # for category in category_list:
            #     db_categories = Category(
            #         name=category['name']
            #     )
            #     print(db_categories)
            #     db_categories.save()

            category_data = data['category']
            if category_data in Category.objects.all():

                db_product_categories = ProductCategories(
                    product=db_product,
                    category=category_data['name'],
                    )
                print(db_product_categories)
                db_product_categories.save()
