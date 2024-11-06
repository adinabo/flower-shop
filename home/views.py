from django.shortcuts import render

def index(request):
    """ return index page view"""
    
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html') 