from django.http.response import Http404, HttpResponseBadRequest
from django.shortcuts import HttpResponse
from rest_framework import status,views
from rest_framework.response import Response
from AgronetApp import serializers
from AgronetApp.models import User
from AgronetApp.serializers import  userSerializer

class userEditView(views.APIView):

    def list(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer=userSerializer(User,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def update(self, request,*args,**kwargs):
        user=self.list(kwargs['username'])
        serializer=userSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

