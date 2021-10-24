from django.db import models
from .product import Product
from .order import Order 
from .user import User
from django.db.models import Sum, F

class OrderDetail(models.Model):
    id_order_detail=models.AutoField(primary_key=True)
    #username_fk2=models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    amount_order=models.IntegerField(null=True)
    id_order_fk=models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    id_product_fk=models.ForeignKey(Product, on_delete=models.DO_NOTHING)  
    def __str__(self):
     return self.id_product_fk
