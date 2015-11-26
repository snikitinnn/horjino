from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'blog/about.html',)

def blog(request):
    return render(request, 'blog/blog.html')

# from django.http.response import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
#
# def about(request):
#     view = 'index'
#     t = get_template('blog/about.html')
#     html = t.render(Context({'name': view}))
#     return HttpResponse(html)
#
# def blog(request):
#     view = 'index'
#     t = get_template('blog/blog.html')
#     html = t.render(Context({'name': view}))
#     return HttpResponse(html)
