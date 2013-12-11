from django import template
from django.template import Context, Template, RequestContext
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
register = template.Library()

@register.simple_tag
def pagination(request, paginator, page, max_pages, method="GET"):
    pages = []
    
    min = page - max_pages if (page - max_pages) > 0 else 1
    max = page + max_pages if (page + max_pages) <= paginator.num_pages else paginator.num_pages
    
    if method == "GET":
        if request.GET:
            params = request.GET.copy()
            if (len(params) > 0 and not 'page' in params) or (len(params) > 1 and 'page' in params):     
                if 'page' in params:
                    del(params['page'])
                
                prefix = "?" + params.urlencode() + "&"
            
            else:
                prefix = "?"
            
        else:
            prefix = "?"
            
        for i in range((max-min)+1):
            num = min+i
            pages += [{'num':num,'url':prefix+'page='+str(num)},]
            
    else:
        for i in range((max-min)+1):
            num = min+i
            url = reverse(method, args=[num])
            pages += [{'num':num,'url':url},]
    
    return render_to_string('tags/pagination.html', {'page_obj':paginator.page(page),
                                                     'pages':pages,
                                                     }, context_instance=RequestContext(request))