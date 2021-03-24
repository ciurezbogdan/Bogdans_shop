from django.db import models
from django.contrib.auth import get_user_model
from Bogdans_shop.models import CustomModel
from products.models import Products

AuthUserModel = get_user_model()

# Create your models here.


class Auction(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    is_winner = models.BooleanField(default=False)
