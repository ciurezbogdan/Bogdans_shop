from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import Profile, Activation, Address
from users.emails import send_activation_email

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)
def create_profile(instance, created, **kwargs):
    if created:
        Profile(user=instance).save()
        Address(user=instance.save())


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(instance, **kwargs):
    if not instance.pk:
        instance.is_active = False
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def activation_details(instance, created, **kwargs):
    if created and not instance.is_active:
        activation = Activation(user=instance)
        activation.save()

        send_activation_email(activation)


