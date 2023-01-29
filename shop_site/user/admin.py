from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



@admin.register(User)
class MyUserAdmin(UserAdmin):
        model = User
        list_display = ('pk','username', 'last_name', 'email', 'get_avatar', 'created_at', 'is_superuser', 'is_active')
        list_display_links = ('pk',)
        list_editable = ('username', 'last_name','email', 'is_superuser', 'is_active')
        list_filter = ('is_superuser','is_active', 'created_at')
        search_fields = ('email', 'username', 'last_name')
        ordering = ('created_at',)
        filter_horizontal = ()
        fieldsets = (
                ("Fields", {
                        'fields': ('email', 'is_staff', 'is_superuser', 'password'),
                }),
        )
