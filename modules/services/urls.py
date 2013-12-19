from django.conf.urls.defaults import *

urlpatterns = patterns('services.views',
    url(r'^$', 'index', name="index"),
    url(r'^(?P<slug>.+)/$', 'details', name="details"),
)