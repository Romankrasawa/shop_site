from django.contrib import admin
from .models import *

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    model = Laptop
    list_display = ("id", "short_characteristics")

@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    model = PC
    list_display = ("id", "short_characteristics")

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    model = Phone
    list_display = ("id", "short_characteristics")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("name", "name_plural")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("code",)

@admin.register(Product_photo)
class Product_photoAdmin(admin.ModelAdmin):
    model = Product_photo
    list_display = ("id", "photo")

