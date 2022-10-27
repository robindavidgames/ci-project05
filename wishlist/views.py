from django.shortcuts import render, get_object_or_404, get_list_or_404
from products.models import Product
from profiles.models import UserProfile
from . models import Wishlist, WishlistItem


def wishlist(request):
    """
    Return a users wishlist.
    """
    user = get_object_or_404(UserProfile, user=request.user)
    print(user)
    wishlist = get_object_or_404(Wishlist, user_profile=user)
    print(wishlist)
    wishlist_item = get_list_or_404(WishlistItem, wishlist=wishlist)
    print(wishlist_item)
    return render(request, 'wishlist/wishlist.html')
