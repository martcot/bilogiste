optima-expert-conseil
===========

Ajoutez un fichier local_settings avec ce qui suit dedans :
```
# important en local seulement
import os, sys
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_PATH, "modules"))

DEBUG=True
COMPRESS_ENABLED = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media") # STATIC_ROOT = "/mnt/media/optimaexpertconseil.ca/"
MEDIA_URL = "/media/" # STATIC_URL = "http://media.optimaexpertconseil.ca/" 

STATIC_ROOT = os.path.join(PROJECT_PATH, "static") # STATIC_ROOT = "/mnt/static/optimaexpertconseil.ca/"
STATIC_URL = "/static/" # STATIC_URL = "http://static.optimaexpertconseil.ca/" 
ADMIN_MEDIA_PREFIX = '/static/admin/' # STATIC_URL = "http://static.optimaexpertconseil/admin/" 

COMPRESS_URL = '/static/' # COMPRESS_URL = "http://static.optimaexpertconseil.ca/"
COMPRESS_ROOT = os.path.join(PROJECT_PATH, "static") #  COMPRESS_ROOT = "/mnt/static/optimaexpertconseil.ca/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'optimaexpertconseil', 
        'USER': 'root',
        'PASSWORD': 'beavis123',
        'HOST': '',
        'PORT': '', 
    }
}

# important en local seulement
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'droberge@d-modules.com'
EMAIL_HOST_PASSWORD = 'droberge1234'
EMAIL_USE_TLS = True

EMAIL_SUFFIX = ' - Optima Expert-Conseil'
SEND_EMAILS_FROM = 'droberge@d-modules.com'
SEND_EMAILS_TO ='droberge@d-modules.com'

```