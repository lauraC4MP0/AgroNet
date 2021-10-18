from django.http.response import Http404
from django.shortcuts import render, HttpResponse
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from agroApp import serializers
from agroApp.models import Product
from agroApp.serializers import ProductSerializer
from agroApp.models.user import User

class ProductsView(views.APIView):

    def get(self, request, *args, **kwargs):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_user(self, usersname):
        try:
            return User.objects.get(pk=usersname)
        except:
            raise Http404

    def post(self,request,*args,**kwargs):
        user=self.get_user(request.data['usersname'])
        Product.objects.create(name_product=request.data['name_product'],descripction_product=request.data['description_prodcut'],price_product=request.data['price_product'],sales_unit_product=request.data['sales_unit_product'],username_fk=user,amount_product=request.data['amount_product'],image_product=request.data['image_product'])
        """serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)"""
        return Response({"message":"producto agregado exitosamente"},status=status.HTTP_201_CREATED)
    
class specificProductView(views.APIView):

    def get_object(self,id_product):
        try:
            return Product.objects.get(pk=id_product)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request,*args,**kwargs):
        product=self.get_object(kwargs['id_product'])
        serializer=ProductSerializer(product)
        return HttpResponse(serializer.data)
        
    def put(self, request,*args,**kwargs):
        product=self.search(kwargs['id_product'])
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,*args,**kwargs):
        product=self.search(kwargs['id_product'])
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
