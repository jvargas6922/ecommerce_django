from django.contrib import admin
from .models import Product
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'stock', 'sale']

admin.site.register(Product, productAdmin)
