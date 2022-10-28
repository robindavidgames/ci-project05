from django.shortcuts import (
    render, get_object_or_404, get_list_or_404,
    redirect, HttpResponse
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from profiles.models import UserProfile
from . models import Wishlist, WishlistItem


@login_required
def wishlist(request):
    """
    Return a users wishlist.
    """
    user = get_object_or_404(UserProfile, user=request.user)
    print(user)
    user_wishlist = get_object_or_404(Wishlist, user_profile=user)
    print(user_wishlist)
    wishlist_item = get_list_or_404(WishlistItem, wishlist=user_wishlist)
    print(wishlist_item)

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

    print(wishlist)
    return redirect(redirect_url)


def remove_from_wishlist(request, item_id):
    """ Remove an item from the wishlist. """

    # bag = request.session.get('bag', {})
    user = get_object_or_404(UserProfile, user=request.user)
    user_wishlist = get_object_or_404(Wishlist, user_profile=user)

    try:
        # Check if item has a variant
        # if 'variant' in request.POST:
        #     variant = request.POST.get('variant')
        #     del bag[item_id]['items_by_variant'][variant]
        #     if not bag[item_id]['items_by_variant']:
        #         bag.pop(item_id)

        # else:
        user_wishlist.pop(item_id)

        messages.success(request, 'Product removed!')
        # request.session['bag'] = bag
        print(user_wishlist)
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
