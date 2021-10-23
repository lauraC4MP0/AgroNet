from django.db import models
from .user import User

class order(models.Model):
    id_order=models.AutoField(primary_key=True)
    date_sale=models.DateTimeField(max_length=30)
    date_delivery=models.DateTimeField(max_length=30)
    username=models.ForeignKey(User,related_name='username',null=False,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)
