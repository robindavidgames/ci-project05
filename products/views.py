from django.shortcuts import render, get_object_or_404
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

def product_view(request, product_id):
    """ A view to return a specific product page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_view.html', context)
