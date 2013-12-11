# -*- coding: UTF-8 -*-
'''from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext_lazy as _

from blog.models import BlogPost
from fab.models import FABPost
from news.models import News
from recipes.models import Recipe

import itertools

class LatestEntriesFeed(Feed):
    title = _(u"Dernières nouvelles - Famillesdaujourdhui.com")
    domain = settings.DOMAIN
    link = "http://"+settings.DOMAIN+"/"
    description = _(u"Dernières nouvelles sur le site de Famillesdaujourdhui.com")

    def items(self):
        results = itertools.chain(
            BlogPost.objects.all().order_by('-pub_date')[:5],
            FABPost.objects.all().order_by('-pub_date')[:5],
            News.objects.all().order_by('-pub_date')[:5],
            Recipe.objects.all().order_by('-pub_date')[:5],
        ) 
        return sorted(results, key=lambda x: x.pub_date, reverse=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
    
    def item_pubdate(self, item):
        return item.pub_date'''