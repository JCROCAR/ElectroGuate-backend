from django.shortcuts import render
from rest_framework import generics, status
from utils.pagination import PaginationData
from rest_framework.response import Response
from orders.models import Order, DetailOrder
from .serializers import OrderSerializerRead, OrderSerializerWrite, DetailOrderSerializerRead, DetailOrderSerializerWrite
from utils import permissions

# Create your views here.

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerWrite
    pagination_class = PaginationData
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES

    def get(self, request, format=None):
        orders = self.get_queryset()
        #Filtro para obtener las 'Orders' según el ID de Usuario ingresado
        orders = orders if request.GET.get('user', None) is None else orders.filter(user =request.GET.get('user'))   
        page = self.paginate_queryset(orders)
        response = Response()
        if page is not None:
            serializer = OrderSerializerRead(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = OrderSerializerRead(page, many=True)
            response.data = serializer.data
            response.status_code = status.HTTP_200_OK
        return response

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerWrite
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES

class DetailOrderList(generics.ListCreateAPIView):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializerWrite
    pagination_class = PaginationData
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES


    def get(self, request, format=None):
        detail_orders = self.get_queryset()
        #Filtro para obtener los 'DetailOrders' según el número de orden ingresada
        detail_orders = detail_orders if request.GET.get('order', None) is None else detail_orders.filter(order =request.GET.get('order'))   
        page = self.paginate_queryset(detail_orders)
        response = Response()
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(detail_orders, many=True)
            response.data = serializer.data
            response.status_code = status.HTTP_200_OK
        return response

class DetailOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializerWrite
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES
