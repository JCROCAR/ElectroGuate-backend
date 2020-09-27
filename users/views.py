from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status, views
from django.conf import settings
from . import models, serializers
from utils.pagination import PaginationData

# Create your views here.


#VISTA DE USUARIOS

#GET Y POST
class UserListAPIView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializerWrite
    pagination_class = PaginationData

#GET, PUT, DELETE
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializerWrite

