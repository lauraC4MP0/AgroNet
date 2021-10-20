from django.http.response import Http404, HttpResponseBadRequest
from django.shortcuts import HttpResponse
from rest_framework import status,views
from rest_framework.response import Response
from AgronetApp import serializers
from AgronetApp.models import user
from AgronetApp.serializers import  userSerializer

class userEditView(views.APIView):

    def get_object(self,usersname):
        try:
            return user.objects.get(pk=usersname)
        except user.DoesNotExist:
            raise Http404

    def put(self, request,*args,**kwargs):
        user=self.search(kwargs['usersname'])
        serializer=userSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
