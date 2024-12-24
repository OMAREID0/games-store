from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GameDetails, Category
from .serializer import CategorySerializer, GameDetailsSerializer

# Create your views here.
@api_view(['GET'])
def getGameByCategoryName(request, name):
    try:
        game = GameDetails.objects.filter(category__name=name)
    except GameDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GameDetailsSerializer(game, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGameByCategoryid(request, id):
    try:
        game = GameDetails.objects.filter(category__id=id)
    except GameDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GameDetailsSerializer(game, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_game(request):
    serializer = GameDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def modify_game(request, pk):
    try:
        game = GameDetails.objects.get(pk=pk)
    except GameDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = GameDetailsSerializer(game)
        return Response(serializer.data)
    
    elif  request.method == 'PUT':
        serializer = GameDetailsSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)