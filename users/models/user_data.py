from django.db import models
from django.contrib.auth import get_user_model
from bogdans_shop.models import CustomModel
from utils.constants import SHIPPING_ADDRESS, BILLING_ADDRESS

# Create your models here.

AuthUserModel = get_user_model()


class Address(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    street = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)

    class Types(models.IntegerChoices):
        SHIPPING = SHIPPING_ADDRESS
        BILLING = BILLING_ADDRESS

    type = models.IntegerField(choices=Types.choices, null=False, default=SHIPPING_ADDRESS)


class Profile(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profiles', default=None, null=True)
