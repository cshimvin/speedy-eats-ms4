from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdminLineItemInline(admin.TabularInline):
    """ Model to display order line items in order admin model """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Model to display order information in admin """
    # Add inline items to order admin:
    inlines = (OrderAdminLineItemInline,)
    # Set admin fields to read only
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total', 'grand_total',
                       'original_bag', 'stripe_pid')
    # display fields in the correct order in admin
    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
              'street_address1', 'street_address2', 'town_or_city', 'county',
              'postcode', 'delivery_cost', 'order_total', 'grand_total',
              'original_bag', 'stripe_pid')
    # Restrict fields to show in list display
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total',)
    # Order by date in reverse order
    ordering = ('-date',)


# register the models

admin.site.register(Order, OrderAdmin)
