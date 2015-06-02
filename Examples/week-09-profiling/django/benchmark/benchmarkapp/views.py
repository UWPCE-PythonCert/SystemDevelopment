from django.shortcuts import render_to_response
from django.template import RequestContext
import md5

def index(request):
    d = {'data': md5.md5("99999999").hexdigest()}
    return render_to_response("index.html", d, context_instance=RequestContext(request))
