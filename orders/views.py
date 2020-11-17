from rest_framework import generics
from utils.pagination import PaginationData
from rest_framework.response import Response
from orders.models import Order, DetailOrder
from .serializers import (
    OrderSerializerWrite,
    DetailOrderSerializerRead,
    DetailOrderSerializerWrite,
)
from utils import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OrderFilter, OrderDetailFilter

# Create your views here.


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerWrite
    pagination_class = PaginationData
    filter_backends =[DjangoFilterBackend]
    filterset_class = OrderFilter
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerWrite
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES


class DetailOrderList(generics.ListCreateAPIView):
    queryset = DetailOrder.objects.all()
    pagination_class = PaginationData
    filter_backends =[DjangoFilterBackend]
    filterset_class = OrderDetailFilter
    serializer_class = {
        "post": DetailOrderSerializerWrite,
        "get": DetailOrderSerializerRead,
    }
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()["get"]
        else:
            return super().get_serializer_class()["post"]


class DetailOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializerWrite
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES
