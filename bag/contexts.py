from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    product_count = 0
    total = 0
    delivery = Decimal(settings.STANDARD_DELIVERY)
    grand_total = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.MINIMUM_ORDER_VALUE:
        minimum_value_met = False
    else:
        minimum_value_met = True

    minimum_order_delta = settings.MINIMUM_ORDER_VALUE - total
    grand_total = total + delivery

    context = {
        'minimum_value_met': minimum_value_met,
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'minimum_order_delta': minimum_order_delta,
        'minimum_order_value': settings.MINIMUM_ORDER_VALUE,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
