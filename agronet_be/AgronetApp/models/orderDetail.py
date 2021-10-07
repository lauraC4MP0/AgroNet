from django.db import models
from .product import Product
from .order import Order 

class OrderDetail(models.Model):
    id_order_detail=models.AutoField(primary_key=True)
    id_product_fk=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    total_price_product=models.DecimalField()
    amount_order=models.IntegerField(null=False)
    id_order_fk=models.ForeignKey(Order,on_delete=models.DO_NOTHING)  
