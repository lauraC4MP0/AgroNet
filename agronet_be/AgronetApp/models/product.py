from django.db import models
from django.db.models.fields import NullBooleanField
from .user import User

class Product(models.Model):
    id_product=models.AutoField(primary_key=True)
    name_product=models.CharField(max_length=30,null=False)
    description_product=models.CharField(max_length=80, null=True)
    price_product=models.IntegerField(null=False)
    sales_unit_product=models.CharField(max_length=20,null=False)
    username_fk=models.ForeignKey(User,on_delete=models.CASCADE)
     #id_order_fk=models.ForeignKey(order,on_delete=models.DO_NOTHING)
    amount_product=models.IntegerField(null=False)
    image_product=models.BinaryField(null=True)
    
    def __str__(self):
        return str(self.username_fk)
     
     #self.email = email
