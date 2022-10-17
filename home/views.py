from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page. """
    # Square bracket limits how many objects are returned.
    best_selling = Product.objects.all().filter(category__name='best-selling')[:4]
    cooking = Product.objects.all().filter(category__name='cooking')[:4]
    context = {
        'best_selling': best_selling,
        'cooking': cooking,
    }

    return render(request, 'home/index.html', context)

