from django_filters import rest_framework as filters
from .models import User


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="str_name", lookup_expr="icontains")
    surname = filters.CharFilter(field_name="str_surname", lookup_expr="icontains")
    email = filters.CharFilter(field_name="str_email", lookup_expr="exact")
    role = name = filters.CharFilter(field_name="str_role", lookup_expr="exact")

    class Meta:
        model = User
        fields = [
            "name",
            "surname",
            "email",
            "role",
            "is_active",
        ]
