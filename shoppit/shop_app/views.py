from django.shortcuts import render
from rest_framework.decorators import api_view
from shop_app.models import Product
from shop_app.serializers import ProductSerializer
from rest_framework.response import Response
# Create your views here.

@api_view("GET")
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


