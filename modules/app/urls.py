# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *
#from app.feeds import LatestEntriesFeed

urlpatterns = patterns('app.views',
    url(r'^$', 'index', name="index"),
    #url(r'^rss/$', LatestEntriesFeed(), name="rss_feed"),
    url(r'^contact/$', 'contact', name="contact"),
)