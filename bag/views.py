from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

# from products.models import Product


def view_bag(request):
    """ A view to return the shopping_bag page. """

    return render(request, 'bag/shopping_bag.html')


# Heavily modified from Boutique Ado project.
def add_to_bag(request, item_id):
    """ Add quantity of an item to the shopping bag. """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Check if item has a variant
    if 'variant' in request.POST:
        variant = request.POST.get('variant')

        # If it has a variant, check if there is already one of that style.
        # If not, add a new item. If so, add one to existing item.
        if item_id in list(bag.keys()):
            if variant in bag[item_id]['items_by_variant'].keys():
                bag[item_id]['items_by_variant'][variant] += quantity
            else:
                bag[item_id]['items_by_variant'][variant] = quantity
        else:
            bag[item_id] = {'items_by_variant': {variant: quantity}}

    # If item doesn't have a variant, create a standard entry.
    # Update item entry, if it is already in the bag.
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    messages.success(request, 'Product added to bag!')
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of an item to the shopping bag. """

    # product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    variant = None
    if 'variant' in request.POST:
        variant = request.POST['variant']

    # Check if item has a variant
    if variant:
        if quantity > 0:
            bag[item_id]['items_by_variant'][variant] = quantity
        else:
            del bag[item_id]['items_by_variant'][variant]

    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    # if variant:
    #     bag[item_id]['items_by_variant'][variant] = quantity

    # else:
    #     bag[item_id] = quantity

    messages.success(request, 'Product quantity adjusted!')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag. """

    bag = request.session.get('bag', {})

    try:
        # Check if item has a variant
        if 'variant' in request.POST:
            variant = request.POST.get('variant')
            del bag[item_id]['items_by_variant'][variant]
            if not bag[item_id]['items_by_variant']:
                bag.pop(item_id)

        else:
            bag.pop(item_id)

        messages.success(request, 'Product removed!')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
