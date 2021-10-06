from django.db import models
from .product import Product
from .order import Order

class OrderDetail(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount=models.IntegerField()
    order_id=models.ForeignKey(Order,on_delete=models.DO_NOTHING)
