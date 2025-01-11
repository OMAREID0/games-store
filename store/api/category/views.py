from rest_framework import viewsets
from .serializers import CategorySerializer, CategoryAddSerializer
from .models import Category
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer 

class CategoryAddViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategoryAddSerializer

class CategoryDetailByIdApiView(APIView):
    def get(self, request, category_id, *args, **kwargs):
        """Retrieve a category by its ID."""
        try:
            category = Category.objects.get(id=category_id)
            data = {
                'id': category.id,
                'name': category.name,
                'description': category.description,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

class CategoryDetailByNameApiView(APIView):
    def get(self, request, category_name, *args, **kwargs):
        """Retrieve a category by its ID."""
        try:
            category = Category.objects.get(name=category_name)
            data = {
                'id': category.id,
                'name': category.name,
                'description': category.description,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)