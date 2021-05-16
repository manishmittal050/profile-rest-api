
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = ['Uses HTTP methods as functions (get, POST, PUT, delete',
        'Is similar to a traditional Django View',]

        return Response({'message':'Hello','an_apiview':an_apiview})

    
    def post(self, request):
        """Creating hello message with our name"""
        serializer = self.serializer_class(data=request.data)
    
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """PUT"""
        return Response({'message':'PUT'})


    def patch(self, request, pk=None):
        """patch"""
        return Response({'message':'patch'})

    def delete(self, request, pk=None):
        """delete"""
        return Response({'message':'delete'})
