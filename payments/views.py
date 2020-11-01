from django.shortcuts import render
from rest_framework import generics, status
from utils.pagination import PaginationData
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializerRead, PaymentSerializerWrite
from utils import permissions

# Create your views here.

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializerWrite
    pagination_class = PaginationData
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES

    def get(self, request, format=None):
        payments = self.get_queryset()
        #Filtro para obtener los 'Payments' según el ID de Usuario ingresado
        payments = payments if request.GET.get('user', None) is None else payments.filter(user =request.GET.get('user'))   
        page = self.paginate_queryset(payments)
        response = Response()
        if page is not None:
            serializer = PaymentSerializerRead(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = PaymentSerializerRead(page, many=True)
            response.data = serializer.data
            response.status_code = status.HTTP_200_OK
        return response

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializerWrite
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES
