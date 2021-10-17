from AgronetApp.models.departament import Departament
from rest_framework import serializers

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = "__all__"

        def create(self, validated_data):
            departamentInstance = Departament.objects.create(**validated_data)
            return departamentInstance

        def to_representation(self, obj):
            departament = Departament.objects.get(id=obj.id)
            return {
                "id_departament" : departament.id_departament,
                "name_departament" : departament.name_departament,
            }