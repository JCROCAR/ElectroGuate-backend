from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status, views
from django.conf import settings
from . import models, serializers
from utils.pagination import PaginationData
from utils import permissions
from django_filters import rest_framework as filters
from .filters import UserFilter
# Create your views here.


#VISTA DE USUARIOS

#GET Y POST
class UserListAPIView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializerRead
    pagination_class = PaginationData
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UserFilter
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES
#Post
class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializerWrite
#GET, PUT, DELETE
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializerWrite
    permission_classes = permissions.DEFAULT_PERMISSIONS_CLASSES

    def put(self, request, pk, format=None):
        response = {
            'status': 'OK',
        }
        httpStatus = status.HTTP_200_OK
        user = models.User.objects.get(id=pk)
        if user is not None:
            serializer = serializers.UserSerializerRead(user, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                response['status'] = 'DATA_ERROR'
                httpStatus = status.HTTP_400_BAD_REQUEST
        else:
            response['status'] = 'DATA_NOT_EXIST'
            httpStatus = status.HTTP_404_NOT_FOUND
        return Response(data=response, status=httpStatus)

