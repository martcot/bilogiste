from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

#from sitemaps import sitemaps

#handler404 = 'app.views.redirection_or_404'

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    #url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
