import django_filters.rest_framework
from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import views
from rest_framework.response import Response
from AgronetApp.serializers import orderDetailSerializer
from AgronetApp.serializers.orderDetailSerializer import OrderDetailSerializer
from AgronetApp.models.orderDetail import OrderDetail
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import generics

class OrderDetailView(generics.ListCreateAPIView):
         queryset = OrderDetail.objects.all()              
         serializer_class = OrderDetailSerializer 

class OrderDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()              
    serializer_class = OrderDetailSerializer

#class OrderDetailView(views.APIView):
 #   permission_classes = (AllowAny,)
 
    
  #  def get(self, request):
   #      Detalle_orden = OrderDetail.objects.all()              
    #     serializer = orderDetailSerializer.OrderDetailSerializer(Detalle_orden, many=True)         
     #    return Response(serializer.data,status=status.HTTP_200_OK)


    #def post(self, request):
     #   Detalle_orden = request.data.get('Detalle_orden')
      #  serializer = orderDetailSerializer.OrderDetailSerializer(data=Detalle_orden)
       # if serializer.is_valid(raise_exception=True):
        #    Detail_saved = serializer.save()
        #return Response(serializer.data,{"success": "Orden Detalle '{}' creada correctamente".format(Detail_saved)})
