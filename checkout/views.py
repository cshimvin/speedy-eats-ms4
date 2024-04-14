from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm
import os


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
        'stripe_public_key': 'pk_test_51OtqHjBRHMXsOWRLrchPAiPXbxwxgOy1TIUodgKxfH02osx29JCP4O78Mv2fKAIJNUu9Xl458zsWsyO0zpOyzkaE00pGFSi6vc',
        'client_secret': 'test',
    }
    return render(request, template, context)
