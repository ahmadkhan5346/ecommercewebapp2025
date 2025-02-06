from django.urls import path
from shop_app import views


urlpatterns = [
    path("products", views.products, name="products")
]