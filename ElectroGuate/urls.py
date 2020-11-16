"""ElectroGuate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


urlpatterns1 = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/products/", include("products.urls")),
    path("api/orders/", include("orders.urls")),
    path("api/payments/", include("payments.urls")),
]
description=""
archivo=open(settings.BASE_DIR+"/ElectroGuate/cambios.md","r")
for linea in archivo:
    description+=linea
schema_view = get_schema_view(
    openapi.Info(
        title="ElectroGuate API",
        default_version="v1",
        description=description,
        terms_of_service="electroguate.me/",
        contact=openapi.Contact(email="contact@electroGuate.local"),
        license=openapi.License(name="Open License"),
    ),
    public=True,
    patterns=urlpatterns1,
    permission_classes=[permissions.AllowAny],
    url="http://127.0.0.1:8000",
)
urlpatterns = urlpatterns1 + [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)