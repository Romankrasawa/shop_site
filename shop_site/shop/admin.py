from django.contrib import admin
from .models import *

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    model = Laptop
    list_display = ("id", "short_characteristics")
