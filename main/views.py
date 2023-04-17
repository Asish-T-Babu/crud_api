from django.shortcuts import render
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def register(request):

    if request.method == 'GET':
        posts = User.objects.all() #querySet
        serialzer = UserSerializer(posts, many=True)
        return Response(serialzer.data)
    
    elif request.method == 'POST':
        serialzer = UserSerializer(data=request.data)

        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','GET'])
def update(request,id):
    user=User.objects.get(id=id)
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data)   

    elif request.method=='PUT':
        serializer=UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors())

@api_view(['DELETE'])
def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return Response('user_deleted')