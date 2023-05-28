# core/management/commands/create_custom_superuser.py
from django.core.management.base import BaseCommand
from authentication.models import CustomUser
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
            print("No user found, creating test user")
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
            if not (password and email):
                raise ValueError('Missing environment variable for superuser creation')
            print('Creating account for %s' % email)

            try:
                admin = CustomUser.objects.create_superuser(email=email, password=password)
                admin.save()
            except:
                raise("Could not create test user")
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
