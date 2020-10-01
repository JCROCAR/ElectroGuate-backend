from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='(Product)'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='(Product)'),
    path('category/', view=views.CategoryList.as_view(),name='(Category)'),
    path('category/<int:pk>/',view=views.CategoryDetail.as_view(),name='(Category)'),
]

