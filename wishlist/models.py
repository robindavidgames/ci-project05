from django.db import models
from products.models import Product
from profiles.models import UserProfile


# Details on Through models from:
# https://docs.djangoproject.com/en/4.1/topics/db/models/#extra-fields-on-many-to-many-relationships

# Some code modified from code in this thread:
# https://code-institute-room.slack.com/archives/C7HS3U3AP/p1613310583353100
class Wishlist(models.Model):
    """
    Model representing user wishlist.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='wishlist'
        )
    products = models.ManyToManyField(Product, through='WishlistItem')

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
        )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='wishlist_products'
        )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
