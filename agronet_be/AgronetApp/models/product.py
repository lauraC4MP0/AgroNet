from django.db import models
from django.db.models.fields import NullBooleanField
from .user import User

class Product(models.Model):
    code=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=80)
    price=models.IntegerField()
    sales_unit=models.CharField(max_length=20)
    id_seller=models.ForeignKey(User,related_name='product',null=False,on_delete=models.CASCADE)
    amount=models.IntegerField()
    image=models.BinaryField(null=True)
