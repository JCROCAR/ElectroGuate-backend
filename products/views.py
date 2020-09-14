from django.shortcuts import render
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
