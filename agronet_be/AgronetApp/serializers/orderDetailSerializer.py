from AgronetApp.models.orderDetail import OrderDetail
from rest_framework import serializers

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"