from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Profile

AuthUserModel = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = AuthUserModel.objects.filter(profile=None).all()
        for user in users:
            Profile(user=user).save()
        print('Added profile to users %s' % len(users))
