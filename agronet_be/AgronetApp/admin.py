from django.contrib import admin
from .models.departament import Departament
from .models.city import City

admin.site.register(Departament)
admin.site.register(City)

# Register your models here.
