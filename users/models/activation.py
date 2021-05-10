from django.db import models
from django.contrib.auth import get_user_model
import secrets
from bogdans_shop.models import CustomModel
from django.utils import timezone
from utils.constants import ACTIVATION_DICT

AuthUserUserModel = get_user_model()


class Activation(CustomModel):
    user = models.OneToOneField(AuthUserUserModel, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, default=secrets.token_hex(32))
    expires_at = models.DateTimeField(default=timezone.now()+timezone.timedelta(**ACTIVATION_DICT))
    activated_at = models.DateTimeField(null=True, default=None)
