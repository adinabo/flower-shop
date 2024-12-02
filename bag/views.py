from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.

def view_bag(request):
    """A view that renders the bag contents page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""
    try:
        # Safely retrieve the quantity and convert it to an integer
        quantity = request.POST.get('quantity')
        if quantity is None:
            raise ValueError("Quantity is missing.")
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
    except (ValueError, TypeError):
        # Handle invalid or missing quantity gracefully
        return HttpResponse("Invalid quantity value.", status=400)

    # Safely retrieve the redirect URL
    redirect_url = request.POST.get('redirect_url', reverse('view_bag'))

    # Retrieve the current bag from the session, or initialize it
    bag = request.session.get('bag', {})

    # Add or update the item quantity in the bag
    bag[item_id] = bag.get(item_id, 0) + quantity

    # Update the session with the modified bag
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    try:
        # Safely retrieve the quantity and convert it to an integer
        quantity = request.POST.get('quantity')
        if quantity is None:
            raise ValueError("Quantity is missing.")
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError("Quantity must be zero or greater.")
    except (ValueError, TypeError) as e:
        # Handle invalid or missing quantity gracefully
        messages.error(request, "Invalid quantity value.")
        return HttpResponse(f"Error: {e}", status=400)

    # Retrieve the current bag from the session
    bag = request.session.get('bag', {})

    # Update or remove the item based on the quantity
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f"Updated quantity for item {item_id} to {quantity}.")
    else:
        if item_id in bag:
            bag.pop(item_id, None)  # Remove the item if quantity is 0
            messages.success(request, f"Removed item {item_id} from your bag.")
        else:
            messages.warning(request, f"Item {item_id} was not found in your bag.")

    # Update the session with the modified bag
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        # Retrieve the current bag from the session
        bag = request.session.get('bag', {})  # Ensure it's a dictionary, not a function
        print("Current bag contents:", bag)  # Debug: log bag contents
        print("Attempting to remove item:", item_id)  # Debug: log item_id

        # Ensure the item_id is treated as a string for comparison
        if str(item_id) in bag:
            bag.pop(str(item_id), None)  # Remove the item
            messages.success(request, f"Removed item {item_id} from your bag.")
        else:
            messages.warning(request, f"Item {item_id} was not found in your bag.")

        # Update the session with the modified bag
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
    
