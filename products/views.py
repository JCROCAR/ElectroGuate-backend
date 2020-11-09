import re
from .models import (
    Product,
    Category,
    Brand,
    Image,
)
from .serializers import (
    ProductSerializer,
    CategorySerializerRead,
    CategorySerializerWrite,
    BrandSerializerWrite,
    BrandSerializerRead,
    ProductListSerializer,
)
from rest_framework import generics, status
from rest_framework.response import Response
from utils import pagination, upload_firebase


# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = {
        "post": ProductListSerializer,
        "get": ProductSerializer,
    }
    pagination_class = pagination.PaginationData

    def create(self, request):
        products = request.data["products"]
        products_response = {"products": []}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            for product in products:
                serializer_product = ProductSerializer(data=product)
                if serializer_product.is_valid():
                    cat = Category(id=product["category"])
                    brd = Brand(id=product["brand"])
                    prod = Product(
                        str_name=product["str_name"],
                        str_description=product["str_description"],
                        str_product_code=product["str_product_code"],
                        int_amount=product["int_amount"],
                        int_price=product["int_price"],
                        category=cat,
                        brand=brd,
                    )
                    prod.save()
                    for image in product["images"]:
                        image_url = upload_firebase.image(
                            name=upload_firebase.decode_image(image["str_image"]),
                            folder="Product",
                        )
                        img = Image(product=prod, str_image=image_url)
                        img.save()
                    products_response["products"].append(ProductSerializer(prod).data)
            return Response(products_response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #

    def get(self, request, format=None):
        products = self.get_queryset()
        # Filtro para obtener los 'productos' según nombre ingresado
        products = (
            products
            if request.GET.get("str_name", None) is None
            else products.filter(str_name=request.GET.get("str_name"))
        )
        page = self.paginate_queryset(products)
        response = Response()
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(products, many=True)
            response.data = serializer.data
            response.status_code = status.HTTP_200_OK
        return response

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()["get"]
        else:
            return super().get_serializer_class()["post"]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerWrite
    pagination_class = pagination.PaginationData


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerRead


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializerWrite
    pagination_class = pagination.PaginationData


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializerRead