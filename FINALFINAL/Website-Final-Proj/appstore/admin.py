from django.contrib import admin

from .models import Product, Customer, Category, Tag, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Order)
