from rest_framework import viewsets
from .serializers import ProductSerializer, ProductAddSerializer
from .models import Product
from api.category.models import Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404



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
            data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'category': product.category.name,
                'price': product.price,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class ProductDetailByCategoryApiView(APIView):
    def get(self, request, category_id, *args, **kwargs):
        """Retrieve a product by its ID."""
        try:
            category = get_object_or_404(Category, id=category_id)
            products = Product.objects.filter(category__name=category)
            serializer = ProductAddSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)