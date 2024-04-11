from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm


def view_checkout(request):
    """ Checkout view """
    bag = request.session.get('bag', {})

    # If bag is empty return an error message
    if not bag:
        messages.error(request, "There are no items in your bag.")
        return redirect(reverse('products'))
    # Create an instance of the order form
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
