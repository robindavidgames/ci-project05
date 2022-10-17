from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.user.username
