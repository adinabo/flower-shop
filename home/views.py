from django.shortcuts import render
from products.models import Product

def index(request):
    
    """Return the index page with a collections section."""
    
    # Fetch random products for each category
    bouquets_products = Product.objects.filter(category__name='bouquets').order_by('?')[:6]
    bridal_products = Product.objects.filter(category__name='bridal').order_by('?')[:6]

    context = {
        'bouquets_products': bouquets_products,
        'bridal_products': bridal_products,
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html') 
