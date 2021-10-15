from AgronetApp.models.orderDetail import OrderDetail
from rest_framework import serializers
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        Model=OrderDetail
        fields=['id_order_detail','id_product','total_price_product','amount_order','id_order']
        #fields = "__all__"
       