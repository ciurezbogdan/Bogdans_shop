from products.models import Products, Category
from django import forms
from django.forms import ModelForm as BaseModelForm


class ProductForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = Products
        fields = ['name', 'price', 'auction_price', 'description', 'image']

    category = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(),
        required=True,
        label='Categories'
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        categories = Category.objects.all()
        category_choices = tuple([(category.id, category.name) for category in categories])
        self.fields['category'].choices = category_choices

    def clean_categories(self):
        categories = self.cleaned_data.get('categories', [])
        try:
            categories = [int(category_id) for category_id in categories]
        except ValueError:
            raise forms.ValidationError('Category IDs must be integers.')
        return categories

    def save(self, commit=True):
        item = super(BaseModelForm, self).save(commit=False)
        item.user = self.user
        item.save()
        return item
