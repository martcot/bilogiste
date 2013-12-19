# -*- coding: utf-8 -*-
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _

from blog.models import BlogPostCategory

class BlogMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        cats = BlogPostCategory.objects.all().order_by('name')
        
        for cat in cats:
            n = NavigationNode(cat.name, cat.get_absolute_url(), cat.id)
            nodes.append(n)
        
        return nodes

menu_pool.register_menu(BlogMenu)