from django.shortcuts import render
from .models import Category, Blog, Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {
        'blogs' : blogs,
        'categories' : categories,
    })

def blog_category(request, category):
    blogs = Blog.objects.filter(category__name__contains=category).order_by('-created_on')
    return render(request, 'blog/blog_category.html', {
        'blogs' : blogs,
        'category' : category,
    })

def blog_detail(request, id):
    blog = Blog.objects.get(pk=id)
    categories = blog.category.all()
    comments = blog.comment_set.all()
    return render(request, 'blog/blog_detail.html', {
        'blog' : blog,
        'categories' : categories,
        'comments' : comments,
    })

def comment(request, id):
    blog = Blog.objects.get(pk=id)
    if request.method == 'POST':
        new_comment = request.POST['comment']
    
    blog.comment_set.create(text=new_comment)
    return HttpResponseRedirect(reverse('blog:blog_detail', args=(blog.id,)))

def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:

        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")

def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:

        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")

def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")

@login_required
def private_place(request):
    return HttpResponse('Sssshhhh, yang ngga berkepentingan dilarang masuk', content_type = 'text/plain')
    
