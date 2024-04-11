from django.shortcuts import (render, redirect,
                              reverse, HttpResponse)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ Display the contents of the shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an amount of a product to the bag """

    # Get values from add to bag form
    product = Product.objects.get(pk=item_id)
    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')

    # Get session information from bag key
    bag = request.session.get('bag', {})

    # Check if item is in the bag dictionary
    if item_id in list(bag.keys()):
        # Increase item by quantity if already in bag
        bag[item_id] += qty
    else:
        # Add item quantity if not in bag
        bag[item_id] = qty
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def alter_bag(request, item_id):
    """ Change the contents of the bag """
    # Get values from add to bag form
    product = Product.objects.get(pk=item_id)
    qty = int(request.POST.get('qty'))

    # Get session information from bag key
    bag = request.session.get('bag', {})

    # Check if item is in the bag dictionary
    if qty > 0:
        bag[item_id] = qty
        messages.success(request,
                         f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the bag """
    # Try to remove item from the bag
    product = Product.objects.get(pk=item_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(request, f'Removed {product.name} from your bag')
        return HttpResponse(status=200)
    # If remove failed, throw an error
    except Exception as e:
        return HttpResponse(status=500)
