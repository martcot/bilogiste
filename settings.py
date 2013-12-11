# -*- coding: utf-8 -*-
import os, sys
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_PATH, "modules"))

try:
    from local_settings import *
except ImportError:
    pass

TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = False

ADMINS = (
     ('Dominic', 'droberge@d-modules.com'),
)

ALLOWED_HOSTS = ['localhost', '127.0.0.1','.d-modules.com']
APPEND_SLASH = True # important pour django-cms

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Montreal'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('fr', gettext('French')),
)

CMS_LANGUAGES = {
    1: [{'code': 'fr',
        'name': gettext('French'),
        'public': True,},
    ],
    'default': {
        'fallbacks': ['fr',],
        'public': False,
    }
}

#CMS_FLAT_URLS = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "base_static"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',          
    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@k6^tq_r#YUFGE(*/*$Y7g8vUF&RDSFIfh546@+%7l--2^^j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'app.context_processors.debug',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "templates"),
)

CMS_TEMPLATES = (
    ("index.html",u"Accueil"),
    ("contact.html",u"Contact"),
    ("content_children.html",u"Contenu - menu enfants"),
    ("content_parent.html",u"Contenu - menu pages soeurs"),
    ("app.html",u"Application"),
)

CMS_SEO_FIELDS = True
CMS_USE_TINYMCE = True
COMPRESS_OUTPUT_DIR = 'compress'

CRISPY_TEMPLATE_PACK = "bootstrap3"

INSTALLED_APPS = (   
    'suit',  
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    
    'cms',
    'cms.plugins.video',
    'cms.plugins.snippet',
    'cms.plugins.picture',
    'cms.plugins.text',
    'ckeditor',
    'menus',
    'south',
    'crispy_forms',
    'mptt',
    'sekizai',
    'compressor',
    'sorl.thumbnail',
    
    'app',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + '/uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':'Full',
        'language':'fr',
    },
}