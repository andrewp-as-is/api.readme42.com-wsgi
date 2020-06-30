import os

from django_configurations_base import BaseConfiguration
from django_configurations_ec2 import EC2Configuration
from django_configurations_github_oauth import GithubOAuthConfiguration

class Base(BaseConfiguration,GithubOAuthConfiguration):
    INSTALLED_APPS_FILE = 'apps.txt'
    INSTALLED_APPS_FIND = True
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.environ['DJANGO_README42_TEMPLATES_PATH']],
        },
    ]

class Dev(Base):
    DEBUG = True

class Prod(Base,EC2Configuration):
    pass
