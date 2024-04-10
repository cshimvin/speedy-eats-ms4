from django.shortcuts import render, redirect, reverse


def view_bag(request):
    """ Display the contents of the shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an amount of a product to the bag """

    # Get values from add to bag form
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

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def alter_bag(request, item_id):
    """ Change the contents of the bag """
    # Get values from add to bag form
    print(request.POST.get('qty'))
    qty = int(request.POST.get('qty'))

    # Get session information from bag key
    bag = request.session.get('bag', {})

    # Check if item is in the bag dictionary
    if qty > 0:
        bag[item_id] = qty
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
