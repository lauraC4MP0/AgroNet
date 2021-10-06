from django.db import models
from .product import Product

class OrderDetail(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product)
    amount=models.IntegerField()
    order_id=models.ForeignKey(Order)
