# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from blog.menu import BlogMenu

class BlogApp(CMSApp):
    name = _(u"Blogue") # give your app a name, this is required
    urls = ["blog.urls"] # link your app to url configuration(s)
    menus = [BlogMenu]

apphook_pool.register(BlogApp) # register your app