# -*- coding: utf-8 -*-
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _

from casestudies.models import CaseStudy

class CaseStudiesMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        cases = CaseStudy.objects.all().order_by('name')
        
        for case in cases:
            n = NavigationNode(case.name, case.get_absolute_url(), case.id)
            nodes.append(n)
        
        return nodes

menu_pool.register_menu(CaseStudiesMenu)
