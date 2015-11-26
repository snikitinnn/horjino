from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context

# Create your views here.
#def index(request):
#    return render(request, 'index.html')

def index(request):
    view = 'index'
    t = get_template('home/index.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

#def base(request):
#    return render(request, 'base.html')