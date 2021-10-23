from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import PasswordField, TokenObtainPairSerializer
from AgronetApp.models.product import Product
from rest_framework import generics

from AgronetApp.serializers.productSerializer import ProductSerializer

class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()              
    serializer_class = ProductSerializer
