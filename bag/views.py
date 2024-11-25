from django.shortcuts import render, redirect, reverse, HttpResponse

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
    except (ValueError, TypeError):
        # Handle invalid or missing quantity gracefully
        return HttpResponse("Invalid quantity value.", status=400)

    # Retrieve the current bag from the session
    bag = request.session.get('bag', {})

    # Update or remove the item based on the quantity
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id, None)  # Remove the item if quantity is 0

    # Update the session with the modified bag
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        # Retrieve the current bag from the session
        bag = request.session.get('bag', {})

        # Remove the specified item from the bag
        bag.pop(item_id, None)

        # Update the session with the modified bag
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
