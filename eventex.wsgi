import os
import sys

sys.path.append('C:\\Projetos\\eventex\\')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()