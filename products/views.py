from django.shortcuts import render
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, status
from rest_framework.response import Response
from utils.pagination import PaginationData


# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationData

    def get(self, request, format=None):
        products = self.get_queryset()
        #Filtro para obtener los 'productos' según nombre ingresado
        products = products if request.GET.get('str_name', None) is None else products.filter(str_name =request.GET.get('str_name'))   
        page = self.paginate_queryset(products)
        response = Response()
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(products, many=True)
            response.data = serializer.data
            response.status_code = status.HTTP_200_OK
        return response

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer