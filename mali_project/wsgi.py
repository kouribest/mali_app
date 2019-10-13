"""
WSGI config for mali_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mali_project.settings")

application = get_wsgi_application()
"""
import os
import sys
 
path = '/home/ubuntu'
if path not in sys.path:
    sys.path.append(path)
 
sys.path.append('/home/ubuntu/mali_project/')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'mali_project.settings'
os.environ['HTTPS'] = "on"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
