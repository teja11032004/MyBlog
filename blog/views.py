from django.shortcuts import render, HttpResponse

# Create your views here.
def blog_home(request):
    return HttpResponse("Welcome to the Blog Home Page!")

def blog_post(request, slug):
    return HttpResponse(f"This is the blog post page for: {slug}")  