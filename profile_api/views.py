from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = ['Uses HTTP methods as functions (get, POST, PUT, delete',
        'Is similar to a traditional Django View',]

        return Response({'message':'Hello','an_apiview':an_apiview})
