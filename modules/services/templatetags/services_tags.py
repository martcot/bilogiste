from django import template
from django.template import Context, Template, RequestContext
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
register = template.Library()

@register.simple_tag
def services_footer(request):
    from services.models import Service
    
    services = Service.objects.all().order_by('name')
    
    return render_to_string('services/footer.html', {'services':services,
                                                     }, context_instance=RequestContext(request))