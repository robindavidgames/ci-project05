import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

# Models in this file modified from Boutique Ado sample project.
class Order(models.Model):
    """
    Model representing user orders.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.CharField(max_length=256, null=False, blank=False)
    phone = models.CharField(max_length=64, null=False, blank=False)
    country = models.CharField(max_length=128, null=False, blank=False)
    postcode = models.CharField(max_length=16, null=True, blank=False)
    town_city = models.CharField(max_length=128, null=False, blank=False)
    street_address_1 = models.CharField(
        max_length=256,
        null=False,
        blank=False
        )
    street_address_2 = models.CharField(
        max_length=256,
        null=False,
        blank=False
        )
    county = models.CharField(max_length=128, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
        )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    
    def _generate_order_number(self):
        """
        Generate an order number using UUID.
        """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        Update the total, accouting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    
    def save(self, *args, **kwargs):
        """
        Overwrite save method to set the order number if it has not aready
        been set.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Model to iterate though and add items to an order.
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
        )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    product_variant = models.CharField(max_length=128, null=True, blank=True)
    order_quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )
    
    def __str__(self):
        return f'SKU {self.product.sku} on {self.order.order_number}'
    
    def save(self, *args, **kwargs):
        """
        Overwrite save method to set the lineiten total and update the order
        total.
        """
        self.lineitem_total = self.product.price *self.order_quantity
        super().save(*args, **kwargs)
