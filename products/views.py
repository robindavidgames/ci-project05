from django.shortcuts import render
from .models import Product

# Create your views here.
# Modified from Boutique Ado project.
def all_products(request):
    """ A view to show all products. """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
