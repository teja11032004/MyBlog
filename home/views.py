from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import post


# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')





def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        if name and email and phone and content:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
        else:
            messages.error(request, "Please fill all fields.")
    return render(request, 'home/contact.html')


# Create your views here.
def search(request):
    query = request.GET.get('query', '')

    allposts = post.objects.filter(title__icontains=query)
    params = {'posts': allposts, 'query': query}
    return render(request, 'home/search.html', params)