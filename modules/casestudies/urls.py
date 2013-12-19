from django.conf.urls.defaults import *

urlpatterns = patterns('casestudies.views',
    url(r'^$', 'index', name="index"),
    url(r'^(?P<slug>.+)/$', 'details', name="details"),
)