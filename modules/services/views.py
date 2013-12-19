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

from services.models import Service

services = Service.objects.all().order_by('name')

def index(request):
    return render_to_response('services/index.html', {"services":services,
                                                      }, context_instance=RequestContext(request))

def details(request, slug):
    try:
        service = Service.objects.get(slug=slug)
        
    except Service.DoesNotExist:
        raise Http404

    return render_to_response('services/details.html', {"services":services,
                                                        "service":service,
                                                        }, context_instance=RequestContext(request))
