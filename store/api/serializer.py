from rest_framework import serializers
from .models import GameDetails, Category



class GameDetailsSerializer(serializers.ModelSerializer):
        class Meta:
            model = GameDetails
            fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = '__all__'