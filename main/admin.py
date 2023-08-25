from django.contrib import admin
from . import models


@admin.register(models.CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'user_status']


@admin.register(models.TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'start_time', 'stop_time']


@admin.register(models.StartTime)
class StartTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'start_time']


@admin.register(models.StopTime)
class StopTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'stop_time']
