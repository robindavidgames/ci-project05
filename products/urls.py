from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<product_id>', views.product_view, name="product_view"),
]
