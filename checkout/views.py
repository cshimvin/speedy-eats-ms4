from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents
import stripe

def view_checkout(request):
    """ Checkout view """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    # If bag is empty return an error message
    if not bag:
        messages.error(request, "There are no items in your bag.")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']

    # Stripe fields
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Create an instance of the order form
    order_form = OrderForm()

    # Check Stripe Public Key is present
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': settings.STRIPE_SECRET_KEY,
    }
    return render(request, template, context)
