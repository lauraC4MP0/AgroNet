from django.db import models
from .departament import Departament

class City(models.Model):
 id_city = models.IntegerField(primary_key=True)
 Departament = models.ForeignKey(Departament, related_name = 'Departamento', on_delete= models.CASCADE)
 name_city = models.CharField('Ciudad', max_length = 30)

 def __str__(self):
        return str(self.name_city)

