from django.urls import path
from . import views

urlpatterns = [
     path(route='users/', view=views.UserListAPIView.as_view(), name='(User)'),
     path(route='users/<int:pk>/', view=views.UserDetailAPIView.as_view(), name='(User)'),

]
