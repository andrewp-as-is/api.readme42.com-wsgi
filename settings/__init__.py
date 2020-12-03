import os

from configurations import values
from django_configurations_autoenv import AutoenvMixin
from django_configurations_base import BaseConfiguration
from django_configurations_ec2 import AllowedHostsMixin, LoggingMixin
from django_configurations_installed_apps import InstalledAppsMixin


class Base(AutoenvMixin, InstalledAppsMixin, BaseConfiguration):
    DATABASES = values.DatabaseURLValue(environ_name='DJANGO_DATABASE_URL')
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.environ['DJANGO_README42_TEMPLATES_PATH']],
        },
    ]


class Dev(Base):
    DEBUG = True


class Prod(AllowedHostsMixin, LoggingMixin, Base):
    DEBUG = False
