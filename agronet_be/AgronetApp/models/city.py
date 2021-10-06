from django.db import models
from .departament import Departamento

class City(models.Model):
id_ciudad = models.AutoField(primary_key=True)
Departamento = models.ForeignKey(departament, related_name = 'Departamento', on_delete= models.CASCADE)
nombre_ciudad = models.CharField('Ciudad', max_lenght = 15)
