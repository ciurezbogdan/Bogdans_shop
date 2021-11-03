from django import forms
from products.models import Products, Category


class ProductDetailsForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = Products
        fields = ['name', 'price', 'auction_price', 'description', 'image', 'category']

    # category = forms.MultipleChoiceField(
    #         widget=forms.CheckboxSelectMultiple,
    #         choices=(),
    #         required=False,
    #         label='Categories'
    #     )
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     categories = Category.objects.all()
    #     category_choices = tuple([(category.id, category.name) for category in categories])
    #     self.fields['category'].choices = category_choices
    #
    # def clean_categories(self):
    #     categories = self.cleaned_data.get('categories', [])
    #     try:
    #         categories = [int(category_id) for category_id in categories]
    #     except ValueError:
    #         raise forms.ValidationError('Category IDs must be integers.')
    #     return categories