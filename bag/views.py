from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_bag(request):
    """ A view to return the shopping_bag page. """

    return render(request, 'bag/shopping_bag.html')

# Heavily modified from Boutique Ado project.
def add_to_bag(request, item_id):
    """ Add quantity of an item to the shopping bag. """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # product_variant = None

    # if 'variant' in request.POST:
    #     product_variant = request.POST('variant')

    bag = request.session.get('bag', {})

    # if product_variant:
    #     if item_id in list(bag.keys()):
    #         if variant in bag[item_id]['items_by_variant'].keys():
    #             bag[item_id]['items_by_variant'][variant] += quantity
    #         else:
    #             bag[item_id]['items_by_variant'][variant] = quantity
    #     else:
    #         bag[item_id] = {'items_by_variant': {variant: quantity}}

    # if 'variant' in request.POST:
        # if item_id in list(bag.keys()):
        #     if variant in bag[item_id]['items_by_variant'].keys():
        #         bag[item_id]['items_by_variant'][variant] += quantity
        #     else:
        #         bag[item_id]['items_by_variant'][variant] = quantity
        # else:
        # product_variant = request.POST('variant')
        # bag[item_id] = {'items_by_variant': {product_variant: quantity}}
    
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

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of an item to the shopping bag. """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    
    # Check if item has a variant
    if 'variant' in request.POST:
        variant = request.POST.get('variant')
        if quantity > 0:
            bag[item_id]['items_by_variant'][variant] = quantity
        else:
            del bag[item_id]['items_by_variant'][variant]

    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
