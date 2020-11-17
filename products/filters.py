from django_filters import rest_framework as filters
from .models import Product, Brand, Category


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="int_price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="int_price", lookup_expr="lte")
    name = filters.CharFilter(field_name="str_name", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = [
            "category",
            "min_price",
            "max_price",
            "name",
            "brand",
        ]


class BrandFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="str_name", lookup_expr="icontains")
    class Meta:
        model = Brand
        fields = [
            "category",
            "name",
        ]


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="str_name", lookup_expr="icontains")
    class Meta:
        model = Category
        fields = [
            "name",
        ]