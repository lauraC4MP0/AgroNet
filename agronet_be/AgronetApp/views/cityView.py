from rest_framework import status,views
from rest_framework.response import Response
from AgronetApp.models.city import City
from AgronetApp.serializers import citySerializer

class CityViews(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = citySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def list(self,request,args,*kwargs):
        orders = City.objects.all()
        serializer = citySerializer(City)
        return Response(serializer.data,status=status.HTTP_200_OK)