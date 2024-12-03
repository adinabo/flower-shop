from django.contrib import admin
from .models import Order, OrderLineItem
from django.db.models.signals import post_save
from django.dispatch import receiver
from checkout.models import Order
from profiles.models import UserProfile

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


@receiver(post_save, sender=Order)
def attach_order_to_profile(sender, instance, created, **kwargs):
    """Automatically attach an order to a user profile upon creation."""
    if created and instance.user_profile is None and instance.user:
        try:
            user_profile = UserProfile.objects.get(user=instance.user)
            instance.user_profile = user_profile
            instance.save()
        except UserProfile.DoesNotExist:
            pass  # No user profile found; skip attaching