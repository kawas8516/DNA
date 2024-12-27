"""
WSGI config for email_subscription project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DNA.settings')

application = get_wsgi_application()


# Run custom setup command
from django.core.management import call_command
try:
    call_command('setup_app')
except Exception as e:
    print(f"Error running setup_app command: {e}")