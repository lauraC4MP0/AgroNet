from AgronetApp.models.city import City
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

        def create(self, validated_data):
            cityInstance = City.objects.create(**validated_data)
            return cityInstance

        def to_representation(self, obj):
            city = City.objects.get(id=obj.id)
            return {
                "id_city" : city.id_city,
                "Departament" : city.Departament,
                "name_city" : city.name_city,
            }