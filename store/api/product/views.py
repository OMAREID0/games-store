from rest_framework import viewsets
from .serializers import ProductSerializer, ProductAddSerializer
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer 

class ProductAddViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductAddSerializer 

class ProductDetailByIdApiView(APIView):
    def get(self, request, product_id, *args, **kwargs):
        """Retrieve a product by its ID."""
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class ProductDetailByCategoryApiView(APIView):
    def get(self, request, Category, *args, **kwargs):
        """Retrieve a product by its ID."""
        try:
            product = Product.objects.get(category=Category)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)