from django.shortcuts import render
from products.models import Product

# def index(request):
#     """ A view to return the index page. """

#     return render(request, 'home/index.html')

def index(request):
    """ A view to return the index page. """
    # products = Product.objects.all()
    # best_selling = products.filter(category__name__in='best-selling')
    # best_selling = products.filter(category__name__in='best-selling')

    # Entry.objects.all().filter(pub_date__year=2006)
    # Entry.objects.filter(pub_date__year=2006)

    best_selling = Product.objects.all().filter(category__name='best-selling')

    context = {
        'best_selling': best_selling,
    }

    return render(request, 'home/index.html', context)

# if 'category' in request.GET:
#             categories = request.GET['category'].split(',')
#             products = products.filter(category__name__in=categories)
#             categories = Category.objects.filter(name__in=categories)
