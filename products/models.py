from django.db import models
from django.contrib.auth import get_user_model
from bogdans_shop.models import CustomModel

AuthUserModel = get_user_model()

# Create your models here.


class Category(CustomModel):
    name = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class ProductCategories(CustomModel):
    product = models.ForeignKey('products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Products(CustomModel):
    class Meta:
        db_table = 'Products'

    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='products', default=None)
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    auction_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    validation = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    category = models.ManyToManyField(Category, through=ProductCategories, related_name='products')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Reviews(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    stars = models.TextField()
    text = models.TextField()


class Questions(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    text = models.TextField()


class Answers(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.TextField()
