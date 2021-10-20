from AgronetApp.models.product import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name_product','description_product','price_product','sales_unit_product','username_fk','amount_product','image_product']

       # def create(self, validated_data):
        #    productInstance = Product.objects.create(**validated_data)
         #   return productInstance

        #def to_representation(self, obj):
         #   product = Product.objects.get(id=obj.id)
          #  return {
           #     "id_product" : product.id_product,
            #    "name_product" : product.name_product,
             #   "description_product" : product.description_product,
              #  "price_product" : product.price_product,
               # "sales_unit_product" : product.sales_unit_product,
                #"username_fk" : product.username_fk,
                #"amount_product" : product.amount_product,
                #"image_product" : product.image_product,
            #}