from rest_framework import status,views
from rest_framework.response import Response
from AgronetApp.models.departament import Departament
from AgronetApp.serializers import departamentSerializer

class DepartamentView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = departamentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def list(self,request,args,*kwargs):
        orders = Departament.objects.all()
        serializer = departamentSerializer(Departament)
        return Response(serializer.data,status=status.HTTP_200_OK)