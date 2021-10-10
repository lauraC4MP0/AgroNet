from AgronetApp.models.city import City
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"