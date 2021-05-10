from django.db import models
from django.contrib.auth import get_user_model
from bogdans_shop.models import CustomModel
from products.models import Products

AuthUserModel = get_user_model()

# Create your models here.


class Orders(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    shipping_address = models.IntegerField()
    billing_address = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)


class OrderProducts(CustomModel):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

