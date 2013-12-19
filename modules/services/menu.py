# -*- coding: utf-8 -*-
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _

from services.models import Service

class ServicesMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        services = Service.objects.all().order_by('name')
        
        for service in services:
            n = NavigationNode(service.name, service.get_absolute_url(), service.id)
            nodes.append(n)
        
        return nodes

menu_pool.register_menu(ServicesMenu)