from django.http.response import Http404
from django.shortcuts import render, HttpResponse
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.serializers import Serializer 
from AgronetApp import serializers
from AgronetApp.models.order import order
from AgronetApp.serializers import orderSerializer
from AgronetApp.models.user import User

class OrdersView(views.APIView):
    def get(self,request,*args,**kwargs):
        orders = order.objects.all()
        serializer = orderSerializer(orders, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def get_user(self, usersname):
        try:
            return User.objects.get(username=request.user.username)
        except:
            raise Http404

   
    def post(self, request, *args, **kwargs):
        user = self.get_user(request.data['username'])
        order.objects.create(date_sale = request.data['date_sale'], date_delivery = request.data['date_delivery'], total_order = request.data['total_order'], username_fk = user)
        return Response({message: "Nuevo pedido agregado exitosamente"}, status = status.HTTP_201_CREATED)
    
class specificOrderView(views.APIView):
    
    def get_object(self,id_order):
        try:
            return order.objects.get(pk = id_order)
        except order.DoesNotExist:
            raise Http404

    def get(self,request,*args,**kwargs):
        order = self.get_object(kwargs['id_order'])
        serializer = orderSerializer(order)
        return HttpResponse(serializer.data)
        
    def put(self, request,*args,**kwargs):
        order =self.search(kwargs['id_order'])
        serializer = orderSerializer(order, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,*args,**kwargs):
        order = self.search(kwargs['id_order'])
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
