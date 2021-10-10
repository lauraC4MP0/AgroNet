from AgronetApp.models.order import order
from rest_framework import serializers

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = "__all__"