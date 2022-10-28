from django.shortcuts import (
    render, get_object_or_404, get_list_or_404,
    redirect, HttpResponse
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from . models import Wishlist, WishlistItem


@login_required
def wishlist(request):
    """
    Return a users wishlist.
    """
    user = get_object_or_404(UserProfile, user=request.user)
    user_wishlist = get_object_or_404(Wishlist, user_profile=user)

    try:
        wishlist_item = get_list_or_404(WishlistItem, wishlist=user_wishlist)

    except:
        wishlist_item = None

    context = {
        'user': user,
        'user_wishlist': user_wishlist,
        'wishlist_item': wishlist_item,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, item_id):
    """ Add an item to the wishlist. """

    redirect_url = request.POST.get('redirect_url')
    user = get_object_or_404(UserProfile, user=request.user)
    user_wishlist = get_object_or_404(Wishlist, user_profile=user)
    user_wishlist.products.add(item_id)
    messages.success(request, 'Product added to your wishlist!')
    return redirect(redirect_url)


def remove_from_wishlist(request, item_id):
    """ Remove an item from the wishlist. """

    user = get_object_or_404(UserProfile, user=request.user)
    user_wishlist = get_object_or_404(Wishlist, user_profile=user)
    user_wishlist.products.remove(item_id)
    messages.success(request, 'Product removed from your wishlist.')
    print(user_wishlist)

    try:
        wishlist_item = get_list_or_404(WishlistItem, wishlist=user_wishlist)

    except:
        wishlist_item = None

    context = {
        'user': user,
        'user_wishlist': user_wishlist,
        'wishlist_item': wishlist_item,
    }

    return render(request, 'wishlist/wishlist.html', context)
