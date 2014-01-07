#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template.loader import render_to_string

from blog.models import BlogPost, BlogPostCategory

cats = BlogPostCategory.objects.all().order_by('name')

def index(request, slug=None):
    if slug == None:
        posts = BlogPost.objects.filter(statut="published").order_by('-id')
        cat = None

    else:
        try:
            cat = BlogPostCategory.objects.get(slug=slug)
            
        except BlogPostCategory.DoesNotExist:
            raise Http404
        
        posts = cat.posts.order_by('-id')
    
    paginator = Paginator(posts, 4)
    try:
        page = int(request.GET.get('page', '1'))
        if page < 1:
            page = 1
        if page > paginator.num_pages:
            page = paginator.num_pages
    except ValueError:
        page = 1
    try:
        page_posts = paginator.page(page)
    except (InvalidPage or EmptyPage):
        raise Http404

    return render_to_response('blog/index.html', {"page_posts":page_posts,
                                                  "page":page,
                                                  "paginator":paginator,
                                                  "cats":cats,
                                                  "cat":cat,
                                                  }, context_instance=RequestContext(request))

def details(request, cat, slug):
    try:
        c = BlogPostCategory.objects.get(slug=cat)
        
    except BlogPostCategory.DoesNotExist:
        raise Http404
    
    try:
        post = BlogPost.objects.get(slug=slug, statut="published", category=c)
        
    except BlogPost.DoesNotExist:
        raise Http404

    return render_to_response('blog/details.html', {"title":post.title,
                                                    "post":post,
                                                    "cats":cats,
                                                    "cat":post.category,
                                                    }, context_instance=RequestContext(request))
