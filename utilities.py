# -*- coding: utf-8 -*-
import re
import ast
from django.core.mail import mail_admins
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from urlparse import urlparse
from django.http import HttpResponse
import unicodedata

def json_repsonse(request, json_content):
    if request.is_ajax():
        # IE 10, FF, Chrome, et autres browser qui marchent...
        return HttpResponse(json_content, mimetype="application/json")
    
    else:
        # IE 9 et plus bas...
        return HttpResponse("<textarea>"+json_content+"</textarea>", mimetype="text/html")

def parse_int(string):
    try:
        return int(string)
    except:
        return None
    
def parse_float(string):
    try:
        return float(string.replace(',','.'))
    except:
        return None
    
def noaasp(string):
    return ''.join((c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn')).replace(' ','_')

def get_tuple_value(tuple,key):
    for k, v in tuple:
        if k == key:
            return unicode(v)
        
    return ""

def truncchar(value, arg):
    if len(value) < arg:
        return value
    else:
        return value[:arg] + '...'
    
def raptf(string):
    print string
    return "\n" + string

def makesellist(objects):
    sel_list = ()
    sel_list +=  (("","--------------------------------"),)
    for obj in objects:
        sel_list +=  ((obj.id,obj),)
    return sel_list
