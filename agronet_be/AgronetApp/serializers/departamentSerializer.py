from AgronetApp.models.departament import Departament
from rest_framework import serializers

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = "__all__"