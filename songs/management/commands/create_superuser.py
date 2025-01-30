import pdb
from os import environ

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser if none exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            username = environ.get('DJANGO_SUPERUSER_USERNAME')
            email = environ.get('DJANGO_SUPERUSER_EMAIL')
            password = environ.get('DJANGO_SUPERUSER_PASSWORD')
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser {username}'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
