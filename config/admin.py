from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib import admin
from config.models import ConfigModel

@admin.register(ConfigModel)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ['enable_auth_token']