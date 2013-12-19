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

from casestudies.models import CaseStudy

cases = CaseStudy.objects.all().order_by('name')

def index(request):
    return render_to_response('casestudies/index.html', {"cases":cases,
                                                         }, context_instance=RequestContext(request))

def details(request, slug):
    try:
        case = CaseStudy.objects.get(slug=slug)
        
    except CaseStudy.DoesNotExist:
        raise Http404

    return render_to_response('casestudies/details.html', {"cases":cases,
                                                           "case":case,
                                                           }, context_instance=RequestContext(request))