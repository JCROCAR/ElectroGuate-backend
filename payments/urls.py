from django.urls import path
from . import views

urlpatterns = [
     path(route='payments/', view=views.PaymentList.as_view(), name='(Payments)'),
     path(route='payments/<int:pk>/', view=views.PaymentDetail.as_view(), name='(Payments)'),
]