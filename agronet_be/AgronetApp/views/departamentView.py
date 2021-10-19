from re import search
from typing import Any
from rest_framework import status,views
from rest_framework.response import Response
from AgronetApp.models.departament import Departament
from AgronetApp.serializers import departamentSerializer
  
from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters




class DepartamentView(views.APIView):

    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter,]
    search_fields = ("id_departament", "name_departament" )
        
    def get(self, request):
         departamento = Departament.objects.all()              
         serializer = departamentSerializer.DepartamentSerializer(departamento, many=True)         
         return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self, request):
        departamento = request.data.get('departamento')
        serializer = departamentSerializer.DepartamentSerializer(data=departamento)
        if serializer.is_valid(raise_exception=True):
            depart_saved = serializer.save()
        return Response({"success": "Departamento '{}' creado correctamente".format(depart_saved)})


 