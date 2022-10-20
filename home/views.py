from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page. """
    # Square bracket limits how many objects are returned.

    sale_items = Product.objects.all().filter(old_price__isnull=False)[:4]
    camping = Product.objects.all().filter(category__name='camping')[:4]
    cooking = Product.objects.all().filter(category__name='cooking')[:4]
    lighting = Product.objects.all().filter(category__name='lighting')[:4]
    navigation = Product.objects.all().filter(category__name='navigation')[:4]
    gadgets = Product.objects.all().filter(category__name='gadgets')[:4]
    hiking = Product.objects.all().filter(category__name='hiking')[:4]
    food_and_drink = Product.objects.all().filter(
        category__name='food_and_drink')[:4]
    context = {
        'sale_items': sale_items,
        'camping': camping,
        'cooking': cooking,
        'lighting': lighting,
        'navigation': navigation,
        'gadgets': gadgets,
        'hiking': hiking,
        'food_and_drink': food_and_drink,
    }

    return render(request, 'home/index.html', context)
