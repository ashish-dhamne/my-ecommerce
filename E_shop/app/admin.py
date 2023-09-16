from django.contrib import admin
from .models import Category,Sub_Category,Product,Contact_us,Order,OrderAdmin,Brand
# Register your models here.

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Contact_us)
admin.site.register(Order, OrderAdmin)
admin.site.register(Brand)




