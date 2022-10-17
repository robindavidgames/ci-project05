from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('order_history/<order_number>', views.order_history, name="order_history"),
    # see add_to_bag for inspiration.
    # path('wishlist/<item_id>/', views.add_to_wishlist, name="add_to_wishlist"),
    path('wishlist/', views.display_wishlist, name="display_wishlist")
]
