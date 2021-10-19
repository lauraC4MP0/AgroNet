from AgronetApp import models
from AgronetApp.models import orderDetail
from AgronetApp.models.orderDetail import OrderDetail
from rest_framework import serializers

class OrderDetailSerializer(serializers.ModelSerializer):
   
    class Meta:
        Model=OrderDetail
        fields=['id_order_detail','id_product','total_price_product','amount_order','id_order']
        
                
    
        
        #fields = "__all__"

        #def create(self, validated_data):
         #   orderdetailInstance = OrderDetail.objects.create(**validated_data)
         #   return orderdetailInstance

       # def to_representation(self, obj):
        #    orderdetail = OrderDetail.objects.get(id=obj.id)
         #   return {
          #      "id_order_detail" : orderdetail.id_order_detail,
           #     "id_product_fk" : orderdetail.id_product_fk,
            #    "total_price_product" : orderdetail.total_price_product,
             #   "amount_order" : orderdetail.amount_order,
              #  "id_order_fk" : orderdetail.id_order_fk,
            #}


       