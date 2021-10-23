from django.db import models
from .product import Product
from .order import order 
from django.db.models import Sum, F

class OrderDetail(models.Model):
    id_order_detail=models.AutoField(primary_key=True)
    id_product_fk=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount_order=models.IntegerField(null=True)
    id_order_fk=models.ForeignKey(order,on_delete=models.DO_NOTHING)  
    def __str__(self):
     return self.id_order_fk
