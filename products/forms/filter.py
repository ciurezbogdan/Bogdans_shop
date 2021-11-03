from django import forms
from django.db import models
from products.models import Category, Products


class OrderBy(models.TextChoices):
    PRICE_ASC = 'price_asc', 'Price ascending'
    PRICE_DESC = 'price_desc', 'Price descending'


class SearchAndFilter(forms.Form):
    search_term = forms.CharField(max_length=255, required=False, label='Search by name')
    order_by = forms.ChoiceField(choices=OrderBy.choices, required=False, label='Order by')
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(),
        required=False,
        label='Categories:'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        category_choices = tuple([(category.id, category.name) for category in categories])
        self.fields['categories'].choices = category_choices

    def clean_ingredients(self):
        categories = self.cleaned_data.get('categories', [])

        try:
            categories = [int(category_id) for category_id in categories]
        except ValueError:
            raise forms.ValidationError('Category IDs must be integers.')

        return categories

    def get_filtered_products(self):
        # with is_valid Django creates the `cleaned_data` dictionary with all the cleaned informations.
        if self.is_valid():
            search_term = self.cleaned_data.get('search_term', None)
            order_by = self.cleaned_data.get('order_by', OrderBy.PRICE_ASC)
            categories = self.cleaned_data.get('categories', [])

            products_list = Products.objects.order_by('-created_at')

            if search_term:
                products_list = products_list.filter(name__icontains=search_term)

            if order_by == OrderBy.PRICE_ASC:
                products_list = products_list.order_by('price')
            elif order_by == OrderBy.PRICE_DESC:
                products_list = products_list.order_by('-price')

            if categories:
                #
                # categories_set = set(categories)
                # product_ids = set()
                # print(categories_set, product_ids)
                # for product in products_list:
                #     product_categories_ids = set([
                #         category_data[0]
                #         for category_data in product.product_category.values_list('category__id')
                #     ])
                #
                #     # if ingredients_set.issubset(pizza_ingredient_ids):
                #     if product_categories_ids.issuperset(categories_set):
                #         product_ids.add(product.id)

                products_list = products_list.filter(category__id__in=categories)

            return products_list

        return Products.objects.all()
