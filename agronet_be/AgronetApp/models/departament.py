from django.db import models

class Departament(models.Model):
    id_departament = models.IntegerField(primary_key=True)
    name_departament = models.CharField('Departamento', max_length = 15)
