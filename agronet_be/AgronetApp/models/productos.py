from django.db import models
from .usuario import User

class productos(models.Model):
    nombre_producto=models.CharField(max_length=20)
    descripcion_producto=models.CharField(max_length=200)
    precio_producto=models.IntegerField()
    univenta_producto=models.CharField(max_length=20)
    cc_vendedor=models.ForeignKey(User,on_delete=models.CASCADE)
    cantidad_producto=models.IntegerField(default=1)
