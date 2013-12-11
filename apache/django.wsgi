import os
import sys
import site

sys.path.append('/mnt/sites/famillesdaujourdhui.com/')
site.addsitedir('/mnt/sites/famillesdaujourdhui.com/python-env/lib/python2.7/site-packages') 

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
