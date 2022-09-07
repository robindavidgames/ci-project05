from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """ A view to return the shopping_bag page. """

    return render(request, 'bag/shopping_bag.html')

# Modified from Boutique Ado project.
def add_to_bag(request, item_id):
    """ Add quantity of an item to the shopping bag. """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)
