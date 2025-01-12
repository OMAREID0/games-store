from rest_framework import serializers
from .models import Category

class CategoryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (('name', 'description'))