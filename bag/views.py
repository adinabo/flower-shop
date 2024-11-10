from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

from django.shortcuts import redirect, get_object_or_404
from products.models import Product

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    # Attempt to get quantity, default to 1 if missing or invalid
    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        quantity = 1  # Default to 1 if quantity is invalid

    redirect_url = request.POST.get('redirect_url', '/')
    bag = request.session.get('bag', {})

    # If item already in bag, increase quantity; otherwise, add it
    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # Update session with new bag contents
    request.session['bag'] = bag
    
    # Redirect to the specified URL or a default page if URL is missing
    return redirect(redirect_url)

    

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    # Try to retrieve and validate quantity; default to 0 if invalid
    try:
        quantity = int(request.POST.get('quantity', 0))
    except (TypeError, ValueError):
        quantity = 0

    bag = request.session.get('bag', {})

    # Adjust the quantity or remove item based on quantity
    if quantity > 0:
        bag[item_id] = quantity  
    else:
        bag.pop(item_id, None)  

    # Update the session with the adjusted bag
    request.session['bag'] = bag
    
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the specified item from the shopping bag"""
    
    try:
        bag = request.session.get('bag', {})

        # Remove the item from the bag
        bag.pop(item_id, None)

        # Update the session with the modified bag
        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)