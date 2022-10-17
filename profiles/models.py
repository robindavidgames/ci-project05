from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from products.models import Product


# Modified from Boutqiue Ado sample project.
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone = models.CharField(max_length=20, null=True, blank=True)
    default_street_address_1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username


# Custom class
class Wishlist(models.Model):
    """
    Wishlist items to iterate through.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    product_variant = models.CharField(max_length=128, null=True, blank=True)
    # added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


# Modified from Boutqiue Ado sample project.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
