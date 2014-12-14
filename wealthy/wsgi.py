"""
WSGI config for wealthy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wealthy.settings")

from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())