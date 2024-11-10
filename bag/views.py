from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    product = get_object_or_404(Product, pk=item_id)  # Retrieve the product or return 404
    quantity = int(request.POST.get('quantity', 1))  # Get the quantity from the form (default is 1 if not provided)
    redirect_url = request.POST.get('redirect_url')  # Get the URL to redirect to after adding to bag
    bag = request.session.get('bag', {})  # Get the current bag session data

    # Check if the product already exists in the bag
    if item_id in bag:
        # If it does, increase the quantity
        bag[item_id] += quantity
    else:
        # Otherwise, add it with the specified quantity
        bag[item_id] = quantity

    # Save the updated bag to the session
    request.session['bag'] = bag
    messages.success(request, f'Added {quantity} x "{product.name}" to your bag.')
    return redirect(redirect_url)
    