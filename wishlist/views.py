from django.shortcuts import render

# Create your views here.
def view_wishlist(request):
    """ A view to return the wishlist page. """

    return render(request, 'wishlist/wishlist.html')
