from django.db import models
from django.db.models.fields import NullBooleanField
from .user import User

class Product(models.Model):
    id_product=models.AutoField(primary_key=True)
    name_product=models.CharField(max_length=30,null=False)
    description_product=models.CharField(max_length=80, null=True)
    price_product=models.IntegerField(null=False)
    sales_unit_product=models.CharField(max_length=20,null=False)
    amount_product=models.IntegerField(null=False)
    image_product=models.BinaryField(null=True)
    username_fk=models.ForeignKey(User,related_name='username2',null=False,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name_product)
     
     #self.email = email
