from django.shortcuts import render, HttpResponse



def home(request):
    return HttpResponse("Welcome to MyBlogg!")

def about(request):
    return HttpResponse("This is the About page of MyBlogg.")   

def contact(request):
    return HttpResponse("This is the Contact page of MyBlogg.") 

# Create your views here.
