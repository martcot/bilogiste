from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name="index"),
    url(r'^(?P<cat>.+)/(?P<slug>.+)/$', 'details', name="details"),
    url(r'^(?P<slug>.+)/$', 'index', name="index"),
)