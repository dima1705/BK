from django.contrib import admin
from .models import Burger
# Register your models here.


@admin.register(Burger)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
    fields = ('name', 'description', 'weight', 'price', 'image')
    search_fields = ('name', 'price')
