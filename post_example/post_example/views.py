'''
Created on May 24, 2017

@author: revathy.sivan
'''
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

@permission_classes((permissions.AllowAny,))
class PostEg(viewsets.ViewSet):
    def create(self, request):
        data = request.data["data"]
        return Response(data)
