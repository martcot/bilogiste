from django import template
from django.template import Context, Template, RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
register = template.Library()

@register.simple_tag
def select_options(request,options,selected_value):
    data = []
    for k,v in options:
        data.append({'val':str(k),'text':v})
    return render_to_string('tags/select_options.html', {'data':data,'value':selected_value}, context_instance=RequestContext(request))