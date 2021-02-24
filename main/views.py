from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/aboutus.html')

def shop(request):
    return render(request, 'main/shop.html')

def blogs(request):
    return render(request, 'main/blogs.html')

def contact(request):
    return render(request, 'main/contactus.html')