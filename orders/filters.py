from django_filters import rest_framework as filters
from .models import Order, DetailOrder


class OrderFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Order
        fields = ["user", "start_date", "end_date"]


class OrderDetailFilter(filters.FilterSet):
    class Meta:
        model = DetailOrder
        fields = ["order"]