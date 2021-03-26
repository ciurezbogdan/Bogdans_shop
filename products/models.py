from django.db import models
from django.contrib.auth import get_user_model
from Bogdans_shop.models import CustomModel

AuthUserModel = get_user_model()

# Create your models here.


class Products(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    auction_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    validation = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')


class Category(CustomModel):
    name = models.CharField(max_length=255, unique=True, null=False)


class ProductCategories(CustomModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


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
