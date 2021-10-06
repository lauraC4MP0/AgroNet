from django.db import models

class Departament(models.Model):
    id _departament = models.AutoField(primary_key=True)
    name_departament = models.CharField('Departamento', max_lenght = 15)
