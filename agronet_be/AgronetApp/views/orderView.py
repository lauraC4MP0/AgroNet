from django.http.response import Http404
from django.shortcuts import render, HttpResponse
from rest_framework import status,views
from rest_framework.response import Response
from agroApp import serializers
from agroApp.models import Order, order
from agroApp.serializers import orderSerializer
from agroApp.models.user import User

class OrdersView(views.APIView):

    def get_user(self, usersname):
        try:
            return User.objects.get(pk=usersname)
        except:
            raise Http404

    def list(self,request,*args,**kwargs):
        orders = Order.objects.all()
        serializer = orderSerializer(orders, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def add(self, request, *args, **kwargs):
        user = self.get_user(request.data['usersname'])
        Order.objects.create(date_sale = request.data['date_sale'], date_delivery = request.data['date_delivery'], total_order = request.data['total_order'], username_fk = user)
        serializer = orderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({message:"Nuevo pedido agregado exitosamente"}, status = status.HTTP_201_CREATED)
    
class specificOrderView(views.APIView):
    
    def search(self,id_order):
        try:
            return Order.objects.get(pk = id_order)
        except Order.DoesNotExist:
            raise Http404

    def searched(self,request,*args,**kwargs):
        order = self.search(kwargs['id_order'])
        serializer = orderSerializer(order)
        return Response(serializer.data)
        
    def update(self, request,*args,**kwargs):
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
    
