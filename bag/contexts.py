from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    """ Context processor to provide shopping bag contents """
    bag = request.session.get('bag', {})
    bag_items = []

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        bag_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity,
        })

    return {'bag_items': bag_items}
