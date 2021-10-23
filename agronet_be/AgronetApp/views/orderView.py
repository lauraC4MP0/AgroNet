from django.http.response import Http404
from django.shortcuts import render, HttpResponse
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.serializers import Serializer 
from AgronetApp import serializers
from AgronetApp.models.order import order
from AgronetApp.serializers import orderSerializer
from AgronetApp.models.user import User

from rest_framework import generics

class OrdersView(generics.ListCreateAPIView):
         queryset = order.objects.all()              
         serializer_class = orderSerializer
         
class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
         queryset = order.objects.all()              
         serializer_class = orderSerializer
