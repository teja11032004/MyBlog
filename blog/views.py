from django.shortcuts import render, HttpResponse
from blog.models import post

# Create your views here.

def blog_home(request):
    allposts= post.objects.all()
    content={'posts': allposts}
    return render(request, 'blog/blog_page.html', content)

def blog_post(request, slug):
    return render(request, 'blog/blog_page.html', {'slug': slug})