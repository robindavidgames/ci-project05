from django.db import models

class Order(models.Model):
    """
    Model representing user orders.
    """
    order_number = models.CharField(max_length=254, null=False, editable=False)
    full_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.CharField(max_length=256, null=False, blank=False)
    phone = models.CharField(max_length=64, null=False, blank=False)
    country = models.CharField(max_length=128, null=False, blank=False)
    postcode = models.CharField(max_length=16, null=True, blank=False)
    town_city = models.CharField(max_length=128, null=False, blank=False)
    street_address_1 = models.CharField(max_length=256, null=False, blank=False)
    street_address_2 = models.CharField(max_length=256, null=False, blank=False)
    county = models.CharField(max_length=128, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
