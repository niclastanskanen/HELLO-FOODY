from django.contrib import admin
from .models import Restaurant, MenuItem, Category, OrderModel


admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
