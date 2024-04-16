from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_order_total_save(sender, instance, created, **kwargs):
    """ Update order total when line item is updated or created """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_order_total_delete(sender, instance, created, **kwargs):
    """ Update order total when line item is deleted """
    instance.order.update_total()
