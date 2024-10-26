from django.shortcuts import render

def index(request):
    """ return index page view"""
    
    return render(request, 'home/index.html')

