from rest_framework import status,views
from rest_framework.response import Response
from AgronetApp.models.city import City
from AgronetApp.serializers import citySerializer

class CityViews(views.APIView):

 
        
    def get(self, request):
         ciudad = City.objects.all()              
         serializer = citySerializer.CitySerializer(ciudad, many=True)         
         return Response(serializer.data,status=status.HTTP_200_OK)