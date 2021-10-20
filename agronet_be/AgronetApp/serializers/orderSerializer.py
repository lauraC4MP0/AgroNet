from AgronetApp.models.order import order
from rest_framework import serializers

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ['date_sale', 'date_delivery', 'total_order','sales_unit','username']

       # def create(self, validated_data):
        #    OrderInstance = order.objects.create(**validated_data)
         #   return OrderInstance

        #def to_representation(self, obj):
         #   Order = order.objects.get(id=obj.id)
          #  return {
           #     "id_order" : Order.id_order,
            #    "date_sale" : Order.date_sale,
             #   "date_delivery" : Order.date_delivery,
              #  "total_order" : Order.total_order,
               # "sales_unit" : Order.sales_unit,
                #"username" : Order.username,
           # }