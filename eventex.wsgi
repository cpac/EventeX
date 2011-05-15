import os
import sys

sys.path.append('C:\\Projetos\\')
os.environ['DJANGO_SETTINGS_MODULE'] = 'eventex.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()