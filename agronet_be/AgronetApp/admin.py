from django.contrib import admin
from .models.departament import Departament
from .models.city import City
from .models.product import Product
from .models.orderDetail import OrderDetail
from .models.order import Order
from .models.user import User


admin.site.register(Departament)
admin.site.register(City)
admin.site.register(Product)
admin.site.register(OrderDetail)
admin.site.register(Order)
admin.site.register(User)

# Register your models here.
