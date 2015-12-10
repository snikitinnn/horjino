# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from forms import PostForms
from models import Post

# Create your views here.
def about(request):
    return render(request, 'blog/about.html',)

def blog(request):
    return render(request, 'blog/blog.html')

def listing(request):
    blog_list = Post.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'blog/listing.html', context)

def news(request):
    blog_list = Post.objects.all()
    blog_list = blog_list.filter(isnews=True).order_by('-pubdate')
    context = {'blog_list': blog_list}
    return render(request, 'blog/news.html', context)

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

# новый пост
def post_new(request):

    if request.method == "POST":
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:listing')# listing
#            return redirect('blog:post_detail', pk = post.pk )# страницы формы
    else:
        form = PostForms
    return render (request, 'blog/post_new.html', {'form':form})

# пост в деталях, иными словами на одной странице
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)


# редактирование поста
def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.id)
    else:
        form = PostForms(instance=post)
    return render(request, 'blog/post_new.html', {'form':form})