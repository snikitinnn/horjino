# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from forms import PostForms
from models import Post,User

# Create your views here.
def about(request):
    return render(request, 'blog/about.html',)

def blog(request):
    return render(request, 'blog/blog.html')

def listing(request):
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    elif request.user.is_superuser==False:
        return redirect('/login/?next=%s' % request.path)

    blog_list = Post.objects.order_by('-pubdate')
    context = {'blog_list': blog_list}
    return render(request, 'blog/listing.html', context)

def news(request):
    blog_list = Post.objects.all()
    blog_list = blog_list.filter(category='news').order_by('-pubdate')
    context = {'blog_list': blog_list}
    return render(request, 'blog/news.html', context)

# новый пост
def post_new(request):
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    elif request.user.is_superuser==False:
        return redirect('/login/?next=%s' % request.path)

    if request.method == "POST":
        form = PostForms(request.POST)
        if form.is_valid():
            user = User.objects.get(id=1)
            post = form.save(commit=False)
            post.user = user
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


from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

class LoginFormView(FormView):
    form_class = AuthenticationForm
    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"
    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)
        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

