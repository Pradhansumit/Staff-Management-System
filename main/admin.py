from django.contrib import admin
from . import models


@admin.register(models.CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'user_status']
