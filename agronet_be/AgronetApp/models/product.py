from django.db import models
from django.db.models.fields import NullBooleanField
from .user import User

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,null=False)
    description=models.CharField(max_length=80, null=True)
    price=models.IntegerField(null=False)
    sales_unit=models.CharField(max_length=20,null=False)
    seller=models.ForeignKey(User,related_name='product',null=False,on_delete=models.CASCADE)
    amount=models.IntegerField(null=False)
    image=models.BinaryField(null=True)
