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
@admin.register(TV)
class TVAdmin(admin.ModelAdmin):
    model = TV
    list_display = ("id", "short_characteristics")

@admin.register(Tablet)
class TabletAdmin(admin.ModelAdmin):
    model = Tablet
    list_display = ("id", "short_characteristics")

@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    model = Monitor
    list_display = ("id", "short_characteristics")

@admin.register(Mouse)
class MouseAdmin(admin.ModelAdmin):
    model = Mouse
    list_display = ("id", "short_characteristics")

@admin.register(Headphones)
class HeadphonesAdmin(admin.ModelAdmin):
    model = Headphones
    list_display = ("id", "short_characteristics")

@admin.register(Keyboard)
class KeuboardAdmin(admin.ModelAdmin):
    model = Keyboard
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

