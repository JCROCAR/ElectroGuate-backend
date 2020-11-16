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
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import ProductFilter, BrandFilter, CategoryFilter

# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = {
        "post": ProductListSerializer,
        "get": ProductSerializer,
    }
    pagination_class = pagination.PaginationData
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ["str_name", "int_price"]

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
                            name=upload_firebase.decode_image(image["url_image"]),
                            folder="Product",
                        )
                        img = Image(product=prod, url_image=image_url)
                        img.save()
                    products_response["products"].append(ProductSerializer(prod).data)
            return Response(products_response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class = CategoryFilter
    ordering_fields = ["str_name"]

    def create(self, request):
        image_url = upload_firebase.image(
            name=upload_firebase.decode_image(request.data["url_image"]),
            folder="Category",
        )
        request.data["url_image"] = image_url
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerRead


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializerWrite
    pagination_class = pagination.PaginationData
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class = BrandFilter
    ordering_fields = ["str_name"]

    def create(self, request):
        image_url = upload_firebase.image(
            name=upload_firebase.decode_image(request.data["url_image"]),
            folder="Brand",
        )
        request.data["url_image"] = image_url
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializerRead