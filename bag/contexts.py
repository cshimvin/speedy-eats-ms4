from django.conf import settings


def bag_contents(request):

    bag_items = []
    product_count = 0
    total = 0
    minimum_order_delta = settings.MINIMUM_ORDER_VALUE - total
    delivery = settings.STANDARD_DELIVERY
    grand_total = total + delivery
    bag = request.session.get('bag', {})

    context = {
        'bag': 'bag',
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'minimum_order_delta': minimum_order_delta,
        'minimum_order_value': settings.MINIMUM_ORDER_VALUE,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
