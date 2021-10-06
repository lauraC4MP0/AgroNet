from django.contrib import admin
from .models.departament import Departament
from .models.city import City
from .models.product import Product
from .models.orderDetail import OrderDetail

admin.site.register(Departament)
admin.site.register(City)
admin.site.register(Product)
admin.site.register(OrderDetail)

# Register your models here.
