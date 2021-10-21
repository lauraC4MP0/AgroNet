from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import PasswordField, TokenObtainPairSerializer
from AgronetApp.models.user import User
from rest_framework import generics
import django_filters.rest_framework

from AgronetApp.serializers.userSerializer import UserSerializer

class UserCreateView(generics.ListCreateAPIView):
         queryset = User.objects.all()              
         serializer_class = UserSerializer
         filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

#class UserCreateView(views.APIView):

    #def post(self, request, *args, **kwargs):
  #      serializer = UserSerializer(data=request.data)
   #     serializer.is_valid(raise_exception=True)
    #    Detail_saved=serializer.save()
        
         #tokenData = {"username":request.data["username"],
         #"password":request.data["password"]}
         #tokenSerializer = TokenObtainPairSerializer(data=tokenData)
         #tokenSerializer.is_valid(raise_exception=True)

        #return Response({"success": "Usuario '{}' creado correctamente".format(Detail_saved)})
       # return Response(tokenSerializer.validated_data,status=status.HTTP_201_CREATED)
