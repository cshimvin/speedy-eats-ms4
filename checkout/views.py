from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents
import stripe


def view_checkout(request):
    """ Checkout view """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)

        # Check form data is valid
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    if isinstance(item_data, int):
                        product = Product.objects.get(id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "We can't find that item. "
                        "Please contact us.")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'Your form data is incorrect \
                Please check your information and try again.')
    else:
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
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order number {order_number} complete. \
        Your food will be delivered in 30 minutes')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
