from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path(route='users/', view=views.UserListAPIView.as_view(), name='(User)'),
     path(route='users/<int:pk>/', view=views.UserDetailAPIView.as_view(), name='(User)'),
     path('login/', obtain_auth_token, name='(login)')

]
