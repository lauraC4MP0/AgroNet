import django_filters.rest_framework
from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import views
from rest_framework.response import Response
from AgronetApp.serializers.orderDetailSerializer import OrderDetailSerializer
from AgronetApp.models.orderDetail import OrderDetail
from rest_framework.permissions import AllowAny



class OrderDetailView(views.APIView):
    
    serializer = OrderDetailSerializer
    QuerySet=OrderDetail.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    
    def get(self, request):
          
          #serializer = OrderDetailSerializer
          #return Response(serializer.data, status=status.HTTP_200_OK)
        #do something with 'GET' method
          return Response("CONEXION GET OK")

    def post(self, request):
        #do something with 'POST' method
        return Response("CONEXION POST OK")
    