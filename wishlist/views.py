from django.shortcuts import render
from products.models import Product
from . models import Wishlist


def view_wishlist(request):
    return render(request, 'wishlist/wishlist.html')

# @login_required
# def view_wishlist(request):
#     if request.method == "POST":
#         if user.is_authenticated:
#             Wishlist.save()
#         else:
#             return HttpResponse("Your request is invalid.")
#     else:
#         return HttpResponse("Your request is invalid.")

#     return render(request, 'wishlist/wishlist.html')


# context = {
#         'form': form,
#         'orders': orders,
#         'profile': profile,
#     }

#     return render(request, template, context)

# @login_required
# def liked(request):
#     if request.method == "POST":
#         if user.is_authenticated:
#             music.save()
#         else:
#             return HttpResponse("Your card is Invalid")
#     else:
#         return HttpResponse("Your request is Invalid")

#     return render(request, template_name='main/wishlist.html', context={"wishlist": Wishlist.objects.all})