from django.db import models

# From Boutique Ado sample project.
class Category(models.Model):

    # To make sure Django admin panel provides the correct name.
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Adapted from Boutique Ado sample project.
class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    overview = models.CharField(max_length=254, null=True, blank=True)
    has_variants = models.BooleanField(default=False, null=True, blank=True)
    variant_one = models.CharField(max_length=254, null=True, blank=True)
    variant_one_stock_quantity = models.IntegerField(null=True, blank=True)
    variant_two = models.CharField(max_length=254, null=True, blank=True)
    variant_two_stock_quantity = models.IntegerField(null=True, blank=True)
    variant_three = models.CharField(max_length=254, null=True, blank=True)
    variant_three_stock_quantity = models.IntegerField(null=True, blank=True)
    stock_quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
        )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
        )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
