from django.urls import path
from . import views

urlpatterns = [
     path(route='orders/', view=views.OrderList.as_view(), name='(Orders)'),
     path(route='orders/<int:pk>/', view=views.OrderDetail.as_view(), name='(Orders)'),
     
     path(route='detail_orders/', view=views.DetailOrderList.as_view(), name='(DetailOrders)'),
     path(route='detail_orders/<int:pk>/', view=views.DetailOrderDetail.as_view(), name='(DetailOrders)'),

]
