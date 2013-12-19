# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from casestudies.menu import CaseStudiesMenu

class CaseStudiesApp(CMSApp):
    name = _(u"Études de cas") # give your app a name, this is required
    urls = ["casestudies.urls"] # link your app to url configuration(s)
    menus = [CaseStudiesMenu]

apphook_pool.register(CaseStudiesApp) # register your app
