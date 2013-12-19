# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from services.menu import ServicesMenu

class ServicesApp(CMSApp):
    name = _(u"Services") # give your app a name, this is required
    urls = ["services.urls"] # link your app to url configuration(s)
    menus = [ServicesMenu]

apphook_pool.register(ServicesApp) # register your app